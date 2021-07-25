from django import forms
from App_Quiz.models import Quiz, QuizQuestion


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuizQuestionForm(forms.ModelForm):
    quiz_wrap = forms.ModelChoiceField(label='New wrap', queryset=Quiz.objects.all())

    def __init__(self, user_id, quiz_id=None, *args, **kwargs):
        super(QuizQuestionForm, self).__init__(*args, **kwargs)
        quizes = Quiz.objects.filter(created_by=user_id)
        choices = [('', '__SELECT QUIZ__')]
        for idx in range(len(quizes)):
            choices.append((f'{quizes[idx].pk}', quizes[idx]))

        if quiz_id is not None:
            self.fields['quiz_wrap'] = forms.ModelChoiceField(label='', required=False, disabled=True,
                                                                    widget=forms.Select(attrs={'hidden': 'true'}),
                                                                    queryset=Quiz.objects.filter(created_by=user_id))
        else:
            if user_id is not None:
                self.fields['quiz_wrap'] = forms.ModelChoiceField(label='Quiz Name', queryset=Quiz.objects.filter(created_by=user_id))

    class Meta:
        model = QuizQuestion
        fields = ('quiz_wrap', 'category', 'quiz_question', 'option1', 'option2', 'option3', 'option4', 'answer', )
        # exclude = ('quiz', 'created_by', )
