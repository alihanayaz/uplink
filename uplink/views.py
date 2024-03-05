from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import UserProfile

# Create your views here.
def index(request):
    return render(request, "index.html")

def account(request):
    return render(request, "account.html")

def login(request):
    return render(request, "login.html")

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
