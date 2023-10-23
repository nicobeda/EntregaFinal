from django.db import models


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
  
    



# Create your models here.
