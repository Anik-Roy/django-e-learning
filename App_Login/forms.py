from django import forms
from App_Login.models import User, Profile
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'is_student', 'is_teacher', )
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3, 'cols': 10})
        }


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', )
