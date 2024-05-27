from .models import Subject, Topic
from django import forms


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'body']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']
