from django.db import models

# Create your models here.
class Category(models.Model):
    """
    category description
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        """
        returns the category name
        """
        return self.friendly_name


class Product(models.Model):
    """
    Product description
    """
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True
    )
    image_url = models.URLField(max_length=2000, null=True, blank=True)
    image = models.ImageField(blank=False)

    def __str__(self):
        """
        returns the product name
        """
        return self.name