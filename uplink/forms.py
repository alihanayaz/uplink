from django import forms
from .models import UserProfile, Link

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'location']

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['title', 'url']