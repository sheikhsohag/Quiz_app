from django.urls import path
from . import views 

urlpatterns = [
     path('quiz/', views.show_quiz, name='showquiz'),
     path('create_quiz/', views.create_quiz, name='createquiz'),
     path('result/', views.result, name='result_result'),
     path('choose_question/', views.choose_question, name='choose_question'),
]
