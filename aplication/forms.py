from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label="Email del usuario")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Correo Electronico")
    password1 = forms.CharField(label="Cambiar contraseña", widget= forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Confirmar contraseña", widget= forms.PasswordInput, required=False) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)   
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)   

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2',]

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)