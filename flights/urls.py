from django.urls import path
from AIR_lines import urls
from . import views


urlpatterns =[
   path("",views.index,name="index"),
   path("<int:flight_id>",views.flight,name="flight"),
   path("<int:flight_id>/book/",views.book,name="book"),
]