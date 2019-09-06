from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('face/new/', views.FaceView.as_view()),
    path('<str:face>/', views.detail, name='detail'),
    # path('<str:face>/<str:emotion>/', views.detail_emotion, name='detail_emotion'),
    path('record/<str:face>/<str:record>/', views.record, name='record'),
    path('record/<str:face>/<str:record>/<str:emotion>/',
         views.record_emotion, name='record_emotion'),
]
