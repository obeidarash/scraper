from django.contrib.auth.models import User
from django.db import models


class ScrapeManager(models.Manager):
    def get_published(self):
        return self.get_queryset().filter(publish=True)

    def get_published_by_id(self, scrape_id):
        return self.get_queryset().filter(publish=True, id=scrape_id).first()


class Scrape(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    url = models.URLField(verbose_name="Link")
    title = models.CharField(max_length=256)
    color = models.CharField(max_length=256)
    size = models.CharField(max_length=256)
    stock = models.IntegerField(verbose_name='In Stock', default=0)
    publish = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)
    objects = ScrapeManager()

    def __str__(self):
        return "{} - {}".format(self.title, self.size)
