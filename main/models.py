from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    CATEGORY_CHOICES = [
        ('baju', 'Baju'),
        ('celana', 'Celana'),
        ('topi', 'Topi'),
        ('sepatu', 'Sepatu'),
        ('update', 'Update')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    is_wanted = models.BooleanField(default=False)
    wishlists = models.PositiveIntegerField(default = 0);

    def __str__(self):
        return self.name

    @property
    def is_item_wanted(self):
        return self.wishlists > 100;
