from django.contrib import admin
from app2.models import person,details
# Register your models here.

class personadmin(admin.ModelAdmin):
    list_display=['id','name','email','phone','age','gender','adhaar']
admin.site.register(person,personadmin)

class detailsadmin(admin.ModelAdmin):
    list_display=['person_ptr_id','name','email','phone','age','gender','adhaar','dno','street','city','state','country','pincode']
admin.site.register(details,detailsadmin)