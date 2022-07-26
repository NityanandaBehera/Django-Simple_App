from email.policy import default
from xml.parsers.expat import model
from django.db import models

# Create your models here.
class UserDetNew(models.Model):
    c= (
        ('Doc','Doctor'),
        ('Patients','Patients')
    )
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    username =  models.CharField(max_length=20,unique=True)
    profile_pic = models.ImageField(upload_to="uploads/pimg/")
    email = models.EmailField(max_length=254,unique=True)
    password =  models.CharField(max_length=200)
    address = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField()
    usertype = models.CharField(max_length=20,choices=c)