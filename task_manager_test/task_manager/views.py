from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import Task
from .forms import TaskForm, ChangeTaskStatusForm, SingUpForm


def signup_view(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('task_list')
    else:
        form = SingUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def task_list(request):
    tasks = Task.objects.order_by('id').all()
    paginator = Paginator(tasks, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'task_list.html', {"page_obj": page_obj})


@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    users = User.objects.all()
    status_choices = Task.Status.choices
    status_form = ChangeTaskStatusForm(request.POST or None, initial={'status': task.status})

    if request.method == 'POST':
        status_form = ChangeTaskStatusForm(request.POST)
        if status_form.is_valid():
            task.status = status_form.cleaned_data['status']
            assigned_to_id = request.POST.get('assigned_to')
            if assigned_to_id:
                task.assigned_to_id = assigned_to_id
            else:
                task.assigned_to = None
            task.save()
            return redirect('task_detail', task_id=task_id)

    return render(request,
                  'task_detail.html',
                  {'task': task,
                   'status_form': status_form,
                   'users': users,
                   'status_choices': status_choices})


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})
