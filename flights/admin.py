from django.contrib import admin
from flights.models import Airport,Flight,Passenger
# Register your models here.


# class AirportAdmin(admin.ModelAdmin):
#     list_display=('code','city')
admin.site.register(Airport)


class FlightAdmin(admin.ModelAdmin):
    list_display=('id','origin','destination','duration')
admin.site.register(Flight,FlightAdmin)


class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal=("flights",)


admin.site.register(Passenger,PassengerAdmin)