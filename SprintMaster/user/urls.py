# urls.py

from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),

    # Other URL patterns
]
