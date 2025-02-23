from django.contrib import admin
from django.urls import path,include
from home import urls
from map import urls
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',include('home.urls')),
    path('',include('map.urls')),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
