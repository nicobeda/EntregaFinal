from django import forms
 
class LecheFormulario(forms.Form):
    marca = forms.CharField()
    precio = forms.IntegerField()
    email = forms.EmailField()