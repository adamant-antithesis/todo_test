from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Task
from .forms import TaskForm, ChangeTaskStatusForm, ChangeTaskTitleDescriptionForm, SingUpForm


def signup_view(request):
    """View function for user registration.

    Renders a registration form and processes POST requests to create a new user.
    Upon successful registration, logs the user in and redirects to the task list page.

    Returns:
        HttpResponse: Rendered registration form template.
    """
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
    """View function for displaying the list of tasks.

    Retrieves all tasks from the database, paginates the list, and renders it on the task list page.

    Returns:
        HttpResponse: Rendered task list template.
    """
    tasks = Task.objects.order_by('id').all()
    paginator = Paginator(tasks, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'task_list.html', {"page_obj": page_obj})


@login_required
def task_detail(request, task_id):
    """View function for displaying the details of a specific task.

    Retrieves the task with the given ID from the database and renders its details along with editable forms
    for modifying its assignee, status, title, and description. Handles form submissions to update the task details
    or delete the task.

    Args:
        request (HttpRequest): The HTTP request object.
        task_id (int): The ID of the task to display.

    Returns:
        HttpResponse: Rendered task detail template.
    """
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return HttpResponseRedirect(reverse('task_list'))
    users = User.objects.all()
    status_choices = Task.Status.choices
    status_form = ChangeTaskStatusForm(request.POST or None,
                                       initial={'status': task.status, 'assigned_to': task.assigned_to})
    title_description_form = ChangeTaskTitleDescriptionForm(request.POST or None,
                                                            initial={'title': task.title,
                                                                     'description': task.description})

    if request.method == 'POST':
        if 'delete_task' in request.POST:
            task.delete()
            return HttpResponseRedirect(reverse('task_list'))

        if status_form.is_valid():
            status_form.save(commit=False)
            task.status = status_form.cleaned_data['status']
            assigned_to_id = status_form.cleaned_data.get('assigned_to')
            if assigned_to_id:
                task.assigned_to_id = assigned_to_id
            else:
                task.assigned_to = None
            task.save()
            return redirect('task_detail', task_id=task_id)

        if title_description_form.is_valid():
            title_description_form.save(commit=False)
            task.title = title_description_form.cleaned_data['title']
            task.description = title_description_form.cleaned_data['description']
            task.save()
            return redirect('task_detail', task_id=task_id)

    return render(request,
                  'task_detail.html',
                  {'task': task,
                   'status_form': status_form,
                   'title_description_form': title_description_form,
                   'users': users,
                   'status_choices': status_choices})


@login_required
def create_task(request):
    """View function for creating a new task.

    Renders a form for creating a new task and processes POST requests to save the new task to the database.

    Returns:
        HttpResponse: Rendered create task form template.
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})
