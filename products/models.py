from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200,)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200,)
    price_range = models.CharField(max_length=100, default="0")
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    image = models.FileField(upload_to='static/products/')

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)