from django.urls import path
from . import views
app_name='map'
urlpatterns = [
    path("maps/", views.maps_view, name="maps"),
]
