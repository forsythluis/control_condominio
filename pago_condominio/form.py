from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Propietario, User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    
class SignupForm(UserCreationForm):
    cedula = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    
    class Meta:
        model = User
        fields = ['cedula', 'nombre', 'apellido', 'username', 'email', 'password1', 'password2']



