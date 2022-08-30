from django.contrib import admin
from .models import Product, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    """
    To create admin display for category Model
    in admin panel
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    """
    To create admin display for Product Model
    in admin panel
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )


admin.site.register(Product, ProductAdmin)
