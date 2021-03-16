from django.db import models
from django.db.models.deletion import SET_NULL
from django.contrib.postgres.fields import ArrayField
# Create your models here.``

class Message(models.Model):
    product = models.ForeignKey("products.Product", on_delete=SET_NULL, related_name="messages", null=True)
    messages = ArrayField(models.JSONField())
    parties = ArrayField(models.IntegerField(), size=2)

