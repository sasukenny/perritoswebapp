from django.db import models
from perritos.models import Perrito
from services.models import hired_service, service

# Create your models here.
class Reportes(models.Model):
    perrito= models.ForeignKey(Perrito,on_delete=models.DO_NOTHING, default=1)
    hired_service= models.OneToOneField(hired_service,on_delete=models.DO_NOTHING, default=1)
    sintomas = models.TextField(default="", null=True)
    ray_x= models.BooleanField(default=False,blank=True)
    ray_x_results= models.TextField(null=True,blank=True)
    ray_x_file = models.FileField(upload_to='files_rayx', null=True)
    blood_test= models.BooleanField(default=False,blank=True)
    blood_test_results= models.TextField(null=True,blank=True)
    blood_test_file= models.FileField(upload_to='files_bloodtest', null=True)
    general_results= models.TextField(null=True,blank=True)
    medicine= models.TextField(null=True,blank=True) 
    
