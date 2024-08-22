from django.urls import path
from .views import create_project, update_project, delete_project

urlpatterns = [
    path('create/', create_project, name='create_project'),
    path('update/<int:pk>/', update_project, name='update_project'),
    path('delete/<int:pk>/', delete_project, name='delete_project'),
    # other paths...
]
