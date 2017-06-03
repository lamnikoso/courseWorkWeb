from django.contrib.auth.models import User
from django import forms

from .models import Profile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('address', 'phone')