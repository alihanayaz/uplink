from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser, UserProfile, Link
from .forms import UserProfileForm, LinkForm, CustomUserCreationForm, CustomPasswordChangeForm
import json

# Create your views here.
def error_404_view(request, exception):
    return render(request, "404.html")

def error_500_view(request):
    return render(request, "500.html")

def index(request):
    return render(request, "index.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
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
    form = CustomUserCreationForm()
    if request.method == "POST":
        username = request.POST.get("username")
        if is_username_inappropriate(username):
            message = "Sorry, we couldn't process your request. Please try again with a different username."
            return render(request, "signup.html", {"form": form, "message": message})

        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('uplink:account')
    return render(request, "signup.html", {"form": form})

def is_username_inappropriate(username):
    inappropriate_words_file = 'uplink/static/data/bad-words-en.json'
    with open(inappropriate_words_file) as json_file:
        inappropriate_words = json.load(json_file)
        return username in inappropriate_words

@login_required
def account(request):
    user = request.user
    links = user.links.all()
    link_limit = 5

    try:
        profile = user.profile
    except UserProfile.DoesNotExist:
        profile = None
        
    profile_form = UserProfileForm(instance=profile)
    link_form = LinkForm()
    password_form = CustomPasswordChangeForm(user)
    
    context = {
        'username': user.username,
        'profile_form': profile_form,
        'link_form': link_form,
        'links': links,
        'password_form': password_form,
    }

    # handle form submissions
    if request.method == "POST":
        if "edit-profile" in request.POST:
            profile_form = UserProfileForm(request.POST, instance=profile)
            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                return redirect('uplink:account')
        if "add-link" in request.POST:
            if links.count() >= link_limit:
                context['add_link_message'] = f'You can only have {link_limit} links.'
                return render(request, "account.html", context)
            link_form = LinkForm(request.POST)
            if link_form.is_valid():
                link = link_form.save(commit=False)
                link.user = user
                link.save()
                return redirect('uplink:account')
        elif "delete-link" in request.POST:
            link_id = request.POST.get("delete-link")
            link = get_object_or_404(Link, id=link_id, user=user)
            link.delete()
            return redirect('uplink:account')
        elif "change-password" in request.POST:
            password_form = CustomPasswordChangeForm(user, request.POST)
            if password_form.is_valid():
                password_form.save()
                return redirect('uplink:account')
            else:
                context['password_form'] = password_form
                return render(request, "account.html", context)
        elif "delete-account" in request.POST:
            user.delete()
            return redirect('uplink:index')


    return render(request, "account.html", context)

def profile(request, name):
    user = get_object_or_404(CustomUser, username=name)

    try:
        profile = user.profile
    except UserProfile.DoesNotExist:
        profile = None

    links = user.links.all()

    context = {
        "name": name,
        "profile": profile,
        "links": links
    }

    return render(request, "profile.html", context)
