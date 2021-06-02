from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from kisii_university import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('staff_management.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
