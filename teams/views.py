from django.shortcuts import render, redirect
from .models import Team,TeamMember
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def team_list(request):
    teams = Team.objects.all()
    return render(request, 'team_list.html', {'teams':teams})

@login_required
def create_team(request):
    if request.method == 'POST':
        name = request.POST['team_name']
        Team.objects.create(team_name = name)
        return redirect('team_list')
    
    return render(request, 'create_team.html')


@login_required
def add_member(request, team_id):
    team = Team.objects.get(id=team_id)
    users = User.objects.all()

    if request.method == "POST":
        user_id = request.POST["user"]
        role = request.POST["role"]

        user = User.objects.get(id=user_id)

        TeamMember.objects.create(
            team=team,
            user=user,
            role=role
        )

        return redirect("team_list")

    return render(request, "add_member.html", {"team": team, "users": users})