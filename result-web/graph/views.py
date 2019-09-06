from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

import json
import numpy as np
from PIL import Image
import base64
from io import BytesIO

from .models import Person, TestPerson
from .database import Database
from rest_framework.response import Response
from rest_framework.views import APIView

COLORS = ['rgb(255, 34, 0)', 'rgb(247, 5, 255)',
            'rgb(243, 193, 245)', 'rgb(152, 255, 92)', 'rgb(164, 166, 162)', 'rgb(103, 240, 215)', 'rgb(2, 196, 15)']
EMOTIONS = ['angry', 'disgusted', 'fearful',
            'happy', 'sad', 'surprised', 'neutral']
local_graph_data = []
isRecord = False

class FaceView(APIView):
    def get(self, request):
        action = request.query_params.get('query')
        db = Database()
        switcher = {
            'get_number_of_rows': db.get_number_of_rows(),
            'get_face_encoding': db.get_face_encoding(),
            'get_all_face': db.get_all_face(),
            'get_graph_local_data': {'local_graph_data': local_graph_data, 'isRecord': isRecord, 'startIndex': len(local_graph_data) - 1}
        }
        res = switcher.get(action, "No request action")
        db.close()
        return Response(res)
    
    def post(self, request):
        db = Database()
        data = request.data
        db.insert(data['face'], data['face_image'], data['face_encoding'])
        db.close()
        return Response("Success")

    def put(self, request):
        global local_graph_data, isRecord
        db = Database()
        data = request.data
        if data['action'] == 'change_face_name':
            db.change_face_name(data['face'], data['newFaceName'])
        elif data['action'] == 'update':
            local_graph_data.append(data)
        elif data['action'] == 'insert_new_record':
            person_id = db.get_primary_key_from_face(data['face'])
            db.insert_new_record(person_id, data['emotion_detail'])
        elif data['action'] == 'setRecord':
            isRecord = data['isRecord']
            local_graph_data = [] if not isRecord else local_graph_data
        db.close()
        return Response("Success")

# Create your views here.
def index(request):
    latest_person_list = TestPerson.objects.all()
    context = {
        'latest_person_list': latest_person_list,
    }
    return render(request, 'graph/index.html', context)

def detail(request, face):
    person = get_object_or_404(TestPerson, face=face)
    record = person.record_set.all()
    # load face image by convert array to image
    image = person.face_image
    image = np.asarray(image, dtype=np.float32)
    img = Image.fromarray(image)
    img = img.convert('RGB')
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()

    record = [r.record_name for r in record]

    return render(request, 'graph/detail.html', {
        'person': person, 
        'img_str': img_str, 
        'color': COLORS,
        'record': record
        })

def record(request, face, record):
    person = get_object_or_404(TestPerson, face=face)
    record = person.record_set.get(record_name=record)
    
    # load face image by convert array to image
    image = person.face_image
    image = np.asarray(image, dtype=np.float32)
    img = Image.fromarray(image)
    img = img.convert('RGB')
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()

    record.emotion_detail = [json.loads(x) for x in record.emotion_detail]
    times, angry, disgusted, fearful, happy, sad, surprised, neutral = (
        [] for i in range(8))
    for i in record.emotion_detail:
        times.append(i['timestamp'])
        angry.append(i['emotion'][0])
        disgusted.append(i['emotion'][1])
        fearful.append(i['emotion'][2])
        happy.append(i['emotion'][3])
        sad.append(i['emotion'][4])
        surprised.append(i['emotion'][5])
        neutral.append(i['emotion'][6])
    summary = [angry, disgusted, fearful, happy, sad, surprised, neutral]

    return render(request, 'graph/record.html', {
        'person': person,
        'img_str': img_str,
        'emotion': ['summary'] + EMOTIONS,
        'path': 'summary',
        'labels': times,
        'data': summary,
        'color': COLORS,
        'emotions': EMOTIONS,
        'record': record.record_name
    })

def record_emotion(request, face, record, emotion):
    emotions = enumerate(EMOTIONS)
    person = get_object_or_404(TestPerson, face=face)
    record = person.record_set.get(record_name=record)

    image = person.face_image
    image = np.asarray(image, dtype=np.float32)
    img = Image.fromarray(image)
    img = img.convert('RGB')
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()

    record.emotion_detail = [json.loads(x) for x in record.emotion_detail]

    times, emotion_arr = ([] for i in range(2))
    index = [idx for idx, e in emotions if e == emotion][0]

    for i in record.emotion_detail:
        times.append(i['timestamp'])
        emotion_arr.append(i['emotion'][index])
    color = COLORS[index]

    return render(request, 'graph/record.html', {
        'person': person,
        'img_str': img_str,
        'emotion': ['summary'] + EMOTIONS,
        'path': emotion,
        'labels': times,
        'data': [emotion_arr],
        'color': [color],
        'emotions': [emotion],
        'record': record.record_name
    })
