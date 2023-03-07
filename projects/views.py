from django.shortcuts import render, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "all_projects": projects,
    }
    return render(request, "projects/project_list.html", context)


@login_required
def redirect_to_home(request):
    return redirect("list_projects")


@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id)

    context = {"project_detail": project}

    return render(request, "projects/detail.html", context)
