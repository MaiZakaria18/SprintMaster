from django.urls import path
from .views import create_task, update_task, delete_task

urlpatterns = [
    path('project/<int:project_id>/tasks/create/',
         create_task, name='create_task'),
    path('project/<int:project_id>/tasks/update/<int:pk>/',
         update_task, name='update_task'),
    path('project/<int:project_id>/tasks/delete/<int:pk>/',
         delete_task, name='delete_task'),
]
