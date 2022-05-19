from django import forms

from .models import *

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'

class SubTaskForm(forms.ModelForm):
    
    class Meta:
        model = SubTask
        exclude = ('task',)