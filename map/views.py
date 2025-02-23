from django.shortcuts import render

def maps_view(request):
    return render(request, "map/maps.html")
