from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, UserProfile, Link

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'location']

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['title', 'url']