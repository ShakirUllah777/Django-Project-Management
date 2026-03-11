from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from projects.models import Project
from teams.models import TeamMember
from tasks.models import Task


def home(request):
    return render(request, "home.html")


def register(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("login")

    return render(request, "register.html")


def user_login(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/users/")

    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def dashboard(request):

    user = request.user

    teams = TeamMember.objects.filter(user=user)
    projects = Project.objects.filter(created_by=user)
    tasks = Task.objects.filter(assigned_to=user)

    context = {
        "teams": teams,
        "projects": projects,
        "tasks": tasks
    }

    return render(request, "dashboard.html", context)