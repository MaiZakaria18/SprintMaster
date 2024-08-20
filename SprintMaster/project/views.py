from django.shortcuts import render, redirect
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required


@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'project/create_project.html', {'form': form})
