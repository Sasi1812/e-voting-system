from django.db import models
class A(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=30)
    vote=models.CharField(max_length=30,default="null")
# Create your models here.
class B(models.Model):
    vote=models.CharField(max_length=40)
    count=models.IntegerField(default=0)