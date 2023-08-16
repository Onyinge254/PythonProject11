from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import TeamLeader

class TeamLeaderRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)
    name = forms.CharField(max_length=100, required=True)
    branch = forms.CharField(max_length=100, required=True)

    class Meta:
        model = TeamLeader
        fields = ['email', 'password1', 'password2', 'name', 'branch']
