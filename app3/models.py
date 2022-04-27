from django.db import models

# Create your models here.

class person(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.BigIntegerField()
    age=models.IntegerField()
    li=[['MALE','Male'],['FEMAIL','Femail']]
    gender=models.CharField(max_length=10,choices=li)
    adhaar=models.CharField(max_length=50)

class details(person):
    dno=models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    pincode=models.IntegerField()

class marks(details):
    ssc=models.IntegerField()
    puc=models.IntegerField()
    ug=models.IntegerField()
    pg=models.IntegerField()
    phd=models.IntegerField()
    raiting=models.IntegerField()