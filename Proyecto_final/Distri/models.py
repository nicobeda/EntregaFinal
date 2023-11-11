from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Leches(models.Model):
    marca= models.CharField(max_length=25)
    precio=models.IntegerField()
    email=models.EmailField(max_length=25)
    


    def __str__(self):
        return f"{self.marca} - {self.precio} -{self.email}"

class Galletitas(models.Model):
    marca= models.CharField(max_length=25)
    precio=models.IntegerField()
    email=models.EmailField(max_length=25)

    def __str__(self):
        return f"{self.marca} - {self.precio} -{self.email}"

class Imag(models.Model):
   
    usua = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='Imag', null=True, blank = True)
 
    def __str__(self):
        return f"{settings.MEDIA_URL} - {self.imagen}"
    



# Create your models here.
