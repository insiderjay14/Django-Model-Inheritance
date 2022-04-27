from django.db import models

# Create your models here.

class payment(models.Model):
    pid=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=50)
    pemail=models.EmailField()
    pphone=models.BigIntegerField()
    dc=models.IntegerField()
    li=[['sbi','SBI'],['union','UNION']]
    bank=models.CharField(max_length=30,choices=li)

class customer(models.Model):
    cid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.BigIntegerField()
    age=models.IntegerField()
    li=[['MALE','Male'],['FEMALE','Female']]
    gender=models.CharField(max_length=10,choices=li)
    adhaar=models.CharField(max_length=20)

class company(customer,payment):
    bal=models.IntegerField()
    
   
