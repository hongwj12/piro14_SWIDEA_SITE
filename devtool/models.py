from django.conf import settings
from django.db import models
from django.urls import reverse


# Create your models here.
class Devtool(models.Model):
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse("devtool:devtool_detail", kwargs={"pk": self.pk})
    