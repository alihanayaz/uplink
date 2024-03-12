from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import CustomUser, UserProfile, Link

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.pop('autofocus', None)

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

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.pop('autofocus', None)

    class Meta:
        model = CustomUser
        fields = ['password']