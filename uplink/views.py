from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile

# Create your views here.
def index(request):
    return render(request, "index.html")

@login_required
def account(request):    
    return render(request, "account.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('uplink:account')
        else:
            return render(request, "login.html", {
                "message": "Invalid credentials."
            })
    else:
        return render(request, "login.html")

@login_required
def logout_view(request):
    logout(request)
    return render(request, "login.html", {
        "message": "Logged out."
    })

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('uplink:account')
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})

def profile(request, name):
    user = get_object_or_404(User, username=name)

    try:
        profile = user.userprofile
    except UserProfile.DoesNotExist:
        profile = None

    links = user.links.all()

    context = {
        "name": name,
        "profile": profile,
        "links": links
    }

    return render(request, "profile.html", context)
