from django import forms
 
class LecheFormulario(forms.Form):
    marca = forms.CharField()
    precio = forms.IntegerField()
    email = forms.EmailField()


class GalleFormulario(forms.Form):
    marca = forms.CharField()
    precio = forms.IntegerField()
    email = forms.EmailField()