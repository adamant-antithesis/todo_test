from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.models import User


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {"tasks": tasks})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})


def assign_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        if user_id:
            user = get_object_or_404(User, pk=user_id)
            task.assigned_to = user
            task.save()
            return redirect('task_list')
    users = User.objects.all()
    return render(request, 'assign_task.html', {'task': task, 'users': users})


def change_task_status(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status:
            task.status = new_status
            task.save()
            return redirect('task_list')
    return render(request, 'change_task_status.html', {'task': task})
