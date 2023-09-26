from django.db import models


# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=250)
    mob_no = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    department = models.CharField(max_length=250)
    courses = models.CharField(max_length=250)
    purpose = models.CharField(max_length=250)
    mat_pro= models.TextField()



def __str__(self):
    return self.name