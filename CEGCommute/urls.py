from zipfile import Path
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from CEGCommute import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('',include('chatapp.urls'))
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
