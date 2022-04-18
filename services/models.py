from django.db import models

from perritos.models import Perrito

# Create your models here.

class service(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='service_pictures', null = True)
    description = models.TextField(max_length=1000)
    price = models.FloatField(default=0.00)
    
class hired_service(models.Model):
    perrito = models.ForeignKey(Perrito, on_delete=models.DO_NOTHING)
    service = models.ForeignKey(service, on_delete=models.DO_NOTHING)
    date_created = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50)
    symptoms_priori = models.TextField(null=True,blank=True)
    
    