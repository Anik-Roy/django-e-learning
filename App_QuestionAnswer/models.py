from django.db import models
from App_Login.models import User
from App_Article.models import Category
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_questions')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_questions')
    title = models.CharField(max_length=100, blank=False, null=False)
    content = RichTextUploadingField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_answers')
    answer = RichTextUploadingField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )


class CommentInAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments_in_answer')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='answer_comments')
    comment = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at', )

