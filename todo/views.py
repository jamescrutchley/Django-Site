from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, reverse

from .models import *
from .forms import *
# Create your views here.


def index(request):
    task_list = Task.objects.all()
    return render(request, "todo/task_list.html", {'task_list':task_list})

def add_task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    return render(request, "todo/add_task.html", {'form':form,})

def edit_task(request,pk):
    task = Task.objects.get(pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    return render(request, "todo/edit_task.html", {'form':form, 'task':task,})

def add_subtask(request,pk):
    task = Task.objects.get(pk=pk)
    form = SubTaskForm()
    if request.method == "POST":
        form =  SubTaskForm(request.POST)
        if form.is_valid():
            subtask = form.save(commit=False)
            subtask.task = task
            form.save()
            return HttpResponseRedirect(f"/edit-task/{subtask.task.id}/")
    return render(request, "todo/add_subtask.html", {'form':form, 'task':task,}) 


def edit_subtask(request,pk):
    subtask = SubTask.objects.get(pk=pk)
    if request.method == "POST":
        subtask.title = request.POST.get("title")
        if request.POST.get("completed") == 'on':
            subtask.completed = True
        else:
            subtask.completed = False
        subtask.save()
    return HttpResponseRedirect(f'/edit-task/{subtask.task.id}/')

        
