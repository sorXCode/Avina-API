from django.db import models
from avina.storage import select_storage
from avina.settings import AUTH_USER_MODEL
from django.db.models.deletion import CASCADE, RESTRICT

class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    category = models.ForeignKey("categories.Category", on_delete=RESTRICT, related_name="product")
    photo1 = models.ImageField(storage=select_storage("/categories"))
    photo2 = models.ImageField(storage=select_storage("/categories"))
    photo3 = models.ImageField(storage=select_storage("/categories"))
    photo4 = models.ImageField(storage=select_storage("/categories"))
    description = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=RESTRICT, related_name="products")
