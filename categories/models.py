from django.db import models
from avina.storage import select_storage
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(storage=select_storage("/categories"))