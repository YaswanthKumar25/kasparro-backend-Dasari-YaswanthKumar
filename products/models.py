from django.db import models

class Product(models.Model):
    external_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
