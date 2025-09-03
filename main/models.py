from django.db import models
import uuid

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('baju', 'Baju'),
        ('celana', 'Celana'),
        ('topi', 'Topi'),
        ('sepatu', 'Sepatu'),
        ('update', 'Update')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField()
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    