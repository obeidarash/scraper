from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from scrape.views import scrape, scrape_detail
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', scrape, name='scrape'),
    path('scrape/<scrape_id>', scrape_detail, name='scrape_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
