import json
import requests

class DatabaseAPI:
  def __init__(self, api):
    self.API = api

  # get number of rows in database
  def get_number_of_rows(self):
    params = {'query': 'get_number_of_rows'}
    r = requests.get(self.API, params=params, headers={'content-type': 'application/json'})
    return int(r.text)

  def get_face_encoding(self):
    params = {'query': 'get_face_encoding'}
    r = requests.get(self.API, params=params, headers={'content-type': 'application/json'})
    return json.loads(r.text)

  # get all rows in face column
  def get_all_face(self):
    params = {'query': 'get_all_face'}
    r = requests.get(self.API, params=params, headers={'content-type': 'application/json'})
    return json.loads(r.text)

  def post(self, payload):
    r = requests.post(self.API, data=json.dumps(payload), headers={'content-type': 'application/json'})
  
  def put(self, payload):
    r = requests.put(self.API, data=json.dumps(payload), headers={'content-type': 'application/json'})
