from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('tasks', views.task_list, name='task_list'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('create/', views.create_task, name='create_task'),
    path('registration/', views.signup_view, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
