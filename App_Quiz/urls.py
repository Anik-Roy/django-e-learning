from django.urls import path
from App_Quiz import views

app_name = 'App_Quiz'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('add-quiz/', views.CreateQuiz.as_view(), name='create_quiz'),
    path('add-quiz-questions/', views.create_quiz_questions, name='create_quiz_questions'),
    path('add-quiz-questions/<quiz_id>/', views.create_quiz_questions, name='create_quiz_questions'),
    path('show-quiz-questions/<quiz_id>/', views.ShowQuizQuestions.as_view(), name='show_quiz_questions'),
    path('show-quiz-answers/<quiz_id>/', views.show_quiz_answers, name='show_quiz_answers'),
]
