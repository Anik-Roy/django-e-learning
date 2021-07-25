from django.db import models
from App_Article.models import Category
from App_Login.models import User

# Create your models here.


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_quizes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# def get_choices():
#     choices = [('', '__SELECT QUIZ__')]
#     quizes = Quiz.objects.all()
#     for idx in range(len(quizes)):
#         choices.append((quizes[idx].pk, quizes[idx]))
#     return choices


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz_questions')
    # quiz_wrap = models.CharField(max_length=100, choices=get_choices())
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_quiz_questions')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_quiz_questions')
    quiz_question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=500)
    option2 = models.CharField(max_length=500)
    option3 = models.CharField(max_length=500)
    option4 = models.CharField(max_length=500)
    lst = (('A', 'option 1'), ('B', 'option 2'), ('C', 'option 3'), ('D', 'option 4'))
    answer = models.CharField(max_length=2, choices=lst, default=lst[0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.quiz_question


