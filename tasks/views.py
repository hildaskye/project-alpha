from django.shortcuts import render, redirect
from tasks.forms import TaskForm
from django.contrib.auth.decorators import login_required
from tasks.models import Task


# Create your views here.
@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect("show_project", item.project.id)
    else:
        form = TaskForm()
    context = {
        "form": form,
    }
    return render(request, "tasks/create.html", context)


@login_required
def task_list(request):
    task_view = Task.objects.filter(assignee=request.user)
    context = {
        "my_tasks": task_view,
    }
    return render(request, "tasks/mytasks.html", context)
