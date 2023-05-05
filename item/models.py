from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)


    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='items_images', blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name