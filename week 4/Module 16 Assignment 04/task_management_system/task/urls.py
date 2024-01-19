from django.urls import path
from .views import show_tasks, add_task, edit_task, delete_task

urlpatterns = [
    path('show-tasks/', show_tasks, name='show_tasks'),
    path('add-task/', add_task, name='add_task'),
    path('edit_task/<int:pk>/', edit_task, name='edit_task'),
    path('delete-task/<int:pk>/', delete_task, name='delete_task'),
]
