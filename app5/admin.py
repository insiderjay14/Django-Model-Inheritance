from django.contrib import admin
from app5.models import customer, payment, company

# Register your models here.
class customeradmin(admin.ModelAdmin):
    list_display=['cid','name','age','email','phone','adhaar','gender']
admin.site.register(customer,customeradmin)

class paymentadmin(admin.ModelAdmin):
    list_display=['pid','pname','pemail','pphone','dc','bank']
admin.site.register(payment,paymentadmin)

class companyadmin(admin.ModelAdmin):
    list_display=['cid','name','age','email','phone','adhaar','gender','pid','pname','pemail','pphone','dc','bank','bal']
admin.site.register(company,companyadmin)

