from django.urls import path
from .views import create_task, update_task, delete_task

urlpatterns = [
    path('task/<int:project_id>/create/',
         create_task, name='create_task'),
    path('task/<int:project_id>/update/<int:pk>/',
         update_task, name='update_task'),
    path('task/<int:project_id>/delete/<int:pk>/',
         delete_task, name='delete_task'),
]
