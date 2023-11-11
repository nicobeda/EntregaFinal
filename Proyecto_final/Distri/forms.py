from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class LecheFormulario(forms.Form):
    marca = forms.CharField()
    precio = forms.IntegerField()
    email = forms.EmailField()
    imagen=forms.ImageField()


class GalleFormulario(forms.Form):
    marca = forms.CharField()
    precio = forms.IntegerField()
    email = forms.EmailField()
    imagen=forms.ImageField()


class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    #password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
    #password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput, required=False)

    last_name = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
   

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name']
