from django.urls import path

from .views import ListProjects, AddProject

urlpatterns = [
    path('projects/', ListProjects, name='list_projects'),
    path('projects/add/', AddProject.as_view(), name='add_project'),

]

