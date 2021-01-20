from django.conf import settings
from django.db import models
from config.utils import uuid_name_upload_to
from django.urls import reverse
from devtool.models import Devtool
# Create your models here.

class Idea(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=uuid_name_upload_to)
    content = models.TextField()
    interest = models.PositiveIntegerField()
    devtool = models.ForeignKey(to=Devtool, related_name="devtool", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("idea:idea_detail", kwargs={"pk": self.pk})
