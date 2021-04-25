from django.db import models
from django.contrib.postgres.fields import ArrayField
from avina.settings import AUTH_USER_MODEL
from django.db.models.deletion import CASCADE, RESTRICT
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
import re
import os
import json
from uuid import uuid4


def generate_uid():
    return uuid4().hex


schools = json.loads(os.getenv("SCHOOLS") or "[]")
schools = [school.lower() for school in schools]

class Product(models.Model):
    uid = models.CharField(default=generate_uid, unique=True, max_length=255)
    name = models.CharField(max_length=255, null=False)
    category = models.ForeignKey(
        "categories.Category", on_delete=RESTRICT, related_name="products")
    photo1 = models.ImageField(upload_to="products")
    photo2 = models.ImageField(upload_to="products")
    photo3 = models.ImageField(upload_to="products")
    photo4 = models.ImageField(upload_to="products")
    description = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=RESTRICT, related_name="products")
    sold = models.BooleanField(default=False)
    tags = ArrayField(models.CharField(max_length=50), default=list)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user_email = get_current_authenticated_user().email

        try:
            school = re.search("@(\w+).", user_email).group(1).lower()
        except AttributeError:
            school = ""

        if school in schools:
            self.tags.append(school)
        
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def __repr__(self):
        return "Product:\t{}\nDescription:\t{}\nStatus:\t{}".format(self.name, self.description, self.status)
