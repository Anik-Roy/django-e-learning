from django import forms
from App_QuestionAnswer.models import Question, Answer, CommentInAnswer

# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = ['title', 'content', ]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = ('user', 'question', )


class CommentInAnswerForm(forms.ModelForm):
    class Meta:
        model = CommentInAnswer
        exclude = ('user', 'answer')

