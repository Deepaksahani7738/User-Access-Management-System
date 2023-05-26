from django.db import models
from django.contrib.auth.models import User

Types=(('Two Wheelers','Two Wheelers'),
       ('Four Wheelers','Four Wheelers'))

class Management_Data(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    vehicle_number=models.CharField(max_length=100)
    vehicle_type=models.CharField(max_length=120,blank=True,null=True,choices=Types)
    vehicle_model=models.TextField()
    vehicle_desc=models.TextField()
    
    def __str__(self):
        return self.vehicle_model
    
# Create your models here.
