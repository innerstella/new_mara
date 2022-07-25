from django.contrib import admin
from .models import Recipe, Category

# Register your models here.
admin.site.register(Recipe)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)