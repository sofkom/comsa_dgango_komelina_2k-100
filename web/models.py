from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Category(models.Model):
    title = models.CharField(max_length=100)

class Review(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='категория')
    text = models.CharField(max_length=1000)


