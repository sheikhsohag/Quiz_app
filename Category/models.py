from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True)
    category_slug = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.category_name