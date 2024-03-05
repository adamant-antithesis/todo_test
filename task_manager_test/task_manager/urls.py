from django.urls import path
from . import views


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('create/', views.create_task, name='create_task'),
    path('registration/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login')
]
