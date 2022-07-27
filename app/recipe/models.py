from tabnanny import verbose
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=10, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'

class Recipe(models.Model):
    title = models.CharField(max_length=20)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    material_1 = models.TextField()
    material_2 = models.TextField()
    material_3 = models.TextField()
    material_4 = models.TextField()
    material_5 = models.TextField()
    material_6 = models.TextField()
    material_7 = models.TextField()
    material_8 = models.TextField()
    material_9 = models.TextField()
    material_10 = models.TextField()

    def __str__(self):
        return self.title