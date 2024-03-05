from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile

# Create your views here.
def index(request):
    return render(request, "index.html")

def account(request):
    if not request.user.is_authenticated:
        return redirect("uplink:login")
    else:
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

def logout_view(request):
    logout(request)
    return render(request, "login.html", {
        "message": "Logged out."
    })

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
