from django.shortcuts import render, redirect
from projects.models import Project


def list_projects(request):
    projects = Project.objects.all()
    context = {
        "all_projects": projects,
    }
    return render(request, "projects/project_list.html", context)


def redirect_to_home(request):
    return redirect("list_projects")
