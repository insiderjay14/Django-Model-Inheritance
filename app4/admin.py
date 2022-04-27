from django.contrib import admin
from app4.models import tech,nontech,stud,person
# Register your models here.

class personadmin(admin.ModelAdmin):
    list_display=['id','name','age','email','phone','adhaar','gender','address','dob','attend']
admin.site.register(person,personadmin)

class techadmin(admin.ModelAdmin):
    list_display=['id','name','age','email','phone','adhaar','gender','address','dob','attend','design','salary','subject']
admin.site.register(tech,techadmin)

class nontechadmin(admin.ModelAdmin):
    list_display=['id','name','age','email','phone','adhaar','gender','address','dob','attend','design','salary']
admin.site.register(nontech,nontechadmin)

class studadmin(admin.ModelAdmin):
    list_display=['id','name','age','email','phone','adhaar','gender','address','dob','attend','course','fee','marks']
admin.site.register(stud,studadmin)