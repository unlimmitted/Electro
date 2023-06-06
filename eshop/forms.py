from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from eshop.models import *

class RegisterUserForm(UserCreationForm):
    username = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={
        'class': 'input100', 'placeholder': 'Логин'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'input100', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Please confirm the entered password', widget=forms.PasswordInput(attrs={
        'class': 'input100', 'placeholder': 'Пожалуйста подтвердите пароль'}))

    class Meta:
        model = User
        fields = {'username', 'password1', 'password2'}


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'input100', 'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'input100', 'placeholder': 'Пароль'}))
    

class AddToCart(forms.ModelForm):
    quantity = forms.IntegerField(label='Количество', widget=forms.TextInput(attrs={'value': '1', 'type': 'hidden'}))

    class Meta:
        model = UserCartList
        fields = ['quantity']