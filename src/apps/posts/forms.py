from .models import Subject, Topic
from django import forms
from django.contrib.auth import authenticate

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'body']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Username", required=True)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, label="Password", required=True)

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Invalid username or password.")
        return self.cleaned_data