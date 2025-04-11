"""defines URL patters for to_do_list"""
from django.urls import path
from . import views

app_name = "to_do_list"
urlpatterns = [
    path('', views.index, name='index'),
    path('task_list/', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]