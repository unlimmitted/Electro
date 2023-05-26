from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'class': 'input-field', 'placeholder': 'Имя'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={
        'class': 'input-field', 'placeholder': 'Фамилия'}))
    username = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={
        'class': 'input-field', 'placeholder': 'Email'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'input-field', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={
        'class': 'input-field', 'placeholder': 'Подтверждение пароля'}))

    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'username', 'password1', 'password2'}


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Email', widget=forms.TextInput(attrs={
        'class': 'input-field', 'placeholder': 'Email'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'input-field', 'placeholder': 'Пароль'}))