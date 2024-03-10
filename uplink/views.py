from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser, UserProfile, Link
from .forms import UserProfileForm, LinkForm, CustomUserCreationForm

# Create your views here.
def index(request):
    return render(request, "index.html")

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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('uplink:account')
    else:
        form = CustomUserCreationForm()
    return render(request, "signup.html", {"form": form})

@login_required
def account(request):
    user = request.user
    links = request.user.links.all()

    # get user profile
    try:
        profile = user.userprofile
    except UserProfile.DoesNotExist:
        profile = None
        
    profile_form = UserProfileForm(instance=profile)

    # handle form submissions
    if request.method == "POST":
        if "edit-profile" in request.POST:
            if profile is not None:
                profile_form = UserProfileForm(request.POST, instance=profile)
            else:
                profile_form = UserProfileForm(request.POST)
            if profile_form.is_valid():
                profile_form.save()
                return redirect('uplink:account')
        if "add-link" in request.POST:
            form = LinkForm(request.POST)
            if form.is_valid():
                link = form.save(commit=False)
                link.user = user
                link.save()
                return redirect('uplink:account')
        elif "delete-link" in request.POST:
            link_id = request.POST.get("delete-link")
            link = get_object_or_404(Link, id=link_id, user=user)
            link.delete()
            return redirect('uplink:account')
    else:
        link_form = LinkForm()

    context = {
        'username': user.username,
        'profile_form': profile_form,
        'link_form': link_form,
        'links': links
    }

    return render(request, "account.html", context)

def profile(request, name):
    user = get_object_or_404(CustomUser, username=name)

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
