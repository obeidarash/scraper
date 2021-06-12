from django.contrib import admin
from .models import Scrape


@admin.register(Scrape)
class ScrapeAdmin(admin.ModelAdmin):
    list_display = ('title', 'color', 'size', 'stock', 'publish')
    list_editable = ('publish',)
