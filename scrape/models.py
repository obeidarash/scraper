from django.contrib.auth.models import User
from django.db import models


class Scrape(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    url = models.URLField(verbose_name="Link")
    title = models.CharField(max_length=256)
    color = models.CharField(max_length=256)
    size = models.CharField(max_length=256)
    stock = models.IntegerField(verbose_name='In Stock', default=0)
    publish = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.size)
