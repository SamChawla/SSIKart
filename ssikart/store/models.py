from django.db import models
from django.urls import reverse
from category.models import Category


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug         = models.SlugField(max_length=200, unique=True)
    description  = models.TextField(max_length=500, blank=True)
    price        = models.IntegerField()
    images       = models.ImageField(upload_to='photos/products')
    stock        = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
    
    def get_url(self):
      return reverse('ssi-product-detail', args=[self.category.slug, self.slug])


variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_variations")
    variation_category = models.CharField(max_length=25, choices=variation_category_choice)
    variation_value = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.product
    
    def __str__(self):
        return f"{self.product}-{self.variation_category}-{self.variation_value}"
    

