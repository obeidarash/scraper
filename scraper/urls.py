from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from scrape.views import scrape
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', scrape, name='scrape'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
