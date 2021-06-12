from django.contrib import admin
from django.urls import path, include
from scrape.views import scrape

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', scrape, name='scrape'),
]
