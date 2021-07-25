from django.urls import path
from App_QuestionAnswer import views

app_name = 'App_QuestionAnswer'

urlpatterns = [
    path('', views.QuestionList.as_view(), name='question_list'),
    path('ask-question', views.CreateQuestion.as_view(), name='ask_question'),
    path('question-detail/<pk>/', views.QuestionDetail.as_view(), name='question_detail'),
]
