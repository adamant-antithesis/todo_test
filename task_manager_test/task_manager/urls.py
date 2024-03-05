from django.urls import path
from . import views


url_patterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('assign/<int:task_id>/', views.assign_task, name='assign_task'),
    path('change-status/<int:task_id>', views.change_task_status, name='change_task_status')
]
