from django.urls import path
import testapp
from .views import *
from django.views.generic import RedirectView

app_name = 'todo'

urlpatterns = [
    path('', index, name='home'), # display list
    path('add-task/',add_task,name='add-task'), # add new tasks
    path('edit-task/<int:pk>/',edit_task,name='edit-task'), # edit tasks
    path('add-subtask/<int:pk>/',add_subtask,name='add-subtask'), # add subtasks to tasks
    path('edit-subtask/<int:pk>/',edit_subtask,name='edit-subtask'), # edit subtasks
]

