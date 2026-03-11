from django.shortcuts import render, redirect
from .models import Project
from teams.models import Team
from django.contrib.auth.decorators import login_required

@login_required
def project_list(request):

    projects = Project.objects.all()

    return render(request, "project_list.html", {"projects": projects})


@login_required
def create_project(request):

    teams = Team.objects.all()

    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        start_date = request.POST["start_date"]
        deadline = request.POST["deadline"]
        team_id = request.POST["team"]

        team = Team.objects.get(id=team_id)

        Project.objects.create(
            name=name,
            description=description,
            start_date=start_date,
            deadline=deadline,
            team=team,
            created_by=request.user
        )

        return redirect("project_list")

    return render(request, "create_project.html", {"teams": teams})