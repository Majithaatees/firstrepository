from django.db import models

# Create your models here.
class mydata(models.Model):
    bname=models.CharField(max_length=20)
    desc=models.CharField(max_length=250)
    contact=models.IntegerField()
class customers(models.Model):
    name=models.CharField(max_length=50)
    uname=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    cpassword=models.CharField(max_length=50)
