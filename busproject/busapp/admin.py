from django.contrib import admin
from busapp.models import Driver
class DriverAdmin(admin.ModelAdmin):
    driverdetails=["drivername","age","contact_no","bus_no"]

admin.site.register(Driver,DriverAdmin)

# Register your models here.
