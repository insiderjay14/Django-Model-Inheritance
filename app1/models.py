from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class base(models.Model):
    name=models.CharField(max_length=50)
    li=[['MALE','Male'],['FEMALE','Female']]
    gender=models.CharField(max_length=10,choices=li)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField()
    attend=models.IntegerField()
    phone=models.BigIntegerField()
    adhaar=models.BigIntegerField()
    dob=models.DateField()
    class Meta:
        abstract=True

class tech(base):
    design=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    salary=models.IntegerField()

class nontech(base):
    design=models.CharField(max_length=20)
    salary=models.IntegerField()

class stud(base):
    course=models.CharField(max_length=20)
    fee=models.IntegerField()
    marks=models.IntegerField()