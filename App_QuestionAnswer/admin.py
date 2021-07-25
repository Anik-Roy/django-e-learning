from django.contrib import admin
from App_QuestionAnswer.models import Question, Answer, CommentInAnswer

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(CommentInAnswer)

