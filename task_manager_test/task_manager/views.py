from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm, ChangeTaskStatusForm
from django.contrib.auth.models import User


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {"tasks": tasks})


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    users = User.objects.all()
    status_choices = Task.Status.choices
    status_form = ChangeTaskStatusForm(request.POST or None, initial={'status': task.status})

    if request.method == 'POST':
        status_form = ChangeTaskStatusForm(request.POST)
        if status_form.is_valid():
            task.status = status_form.cleaned_data['status']
            task.save()
            return redirect('task_detail', task_id=task_id)

    return render(request,
                  'task_detail.html',
                  {'task': task,
                   'status_form': status_form,
                   'users': users,
                   'status_choices': status_choices})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})
