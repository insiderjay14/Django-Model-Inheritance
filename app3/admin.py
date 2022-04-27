from django.contrib import admin
from app3.models import person,details,marks

# Register your models here.

class personadmin(admin.ModelAdmin):
    list_display=['id','name','email','phone','age','gender','adhaar']
admin.site.register(person,personadmin)

class detailsadmin(admin.ModelAdmin):
    list_display=['person_ptr_id','name','email','phone','age','gender','adhaar','dno','street','city','state','country','pincode']
admin.site.register(details,detailsadmin)

# class marksadmin(admin.ModelAdmin):
#     list_display=['person_ptr_id','details_ptr_id','name','email','phone','age','gender','adhaar','dno','street','city','state','country','pincode','ssc','puc','ug','pg','phd','raiting']
# admin.site.register(marks,marksadmin)