from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Perrito(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='pictures', null = True)
    birth = models.DateField(null=True, blank=True)
    #registerDay = models.DateTimeField(auto_created=True, blank=True)
    # genero 0 para macho y 1 para hembra
    gender = models.CharField(default='no definido', max_length=50)
    race = models.CharField(max_length=200, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # codigo = models.CharField(unique=True, auto_created= True, blank=True, max_length=200)