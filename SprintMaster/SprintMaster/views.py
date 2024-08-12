from django.http import HttpResponse
from django.shortcuts import render


def SprintMaster(request):
    return render(request, 'layout.html')


def project(request):
    return render(request, 'project_list.html')







