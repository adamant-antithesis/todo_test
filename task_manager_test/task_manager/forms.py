from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'assigned_to']


class ChangeTaskStatusForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status', 'assigned_to']
