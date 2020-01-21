from django.contrib import admin
from .models import Doctor,Reservation
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display=('name', 'city', 'featured', 'area','speciality')
    list_display_links=('name',)
    list_filter=('city','area')
    list_editable=('featured','speciality')

class BookingAdmin(admin.ModelAdmin):
    list_display=('doctor', 'name','date','time')
    list_display_links=('doctor','name')
    list_filter=('doctor', 'date')

    
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Reservation, BookingAdmin)