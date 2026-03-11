from django.shortcuts import render, redirect
from .models import Task
from projects.models import Project
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def task_list(request):

    tasks = Task.objects.all()

    return render(request, "task_list.html", {"tasks": tasks})


@login_required
def create_task(request):

    projects = Project.objects.all()
    users = User.objects.all()

    if request.method == "POST":

        title = request.POST.get("title")
        description = request.POST.get("description")
        project_id = request.POST.get("project")
        user_id = request.POST.get("assigned_to")
        start_date = request.POST.get("start_date")
        due_date = request.POST.get("due_date")
        priority = request.POST.get("priority")

        project = Project.objects.get(id=project_id)
        user = User.objects.get(id=user_id)

        Task.objects.create(
            title=title,
            description=description,
            project=project,
            assigned_to=user,
            start_date=start_date,
            due_date=due_date,
            priority=priority
        )

        return redirect("task_list")

    return render(request, "create_task.html", {"projects": projects, "users": users})

@login_required
def update_task_status(request, task_id):

    task = Task.objects.get(id=task_id)

    if request.method == "POST":
        status = request.POST.get("status")
        task.status = status
        task.save()

    return redirect("task_list")