from django.contrib import admin
from .models import Category, Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
   list_display = ('id','name', 'desc',)

class ProductAdmin(admin.ModelAdmin):
   list_display = ('id','name', 'desc','price_range','cat_name')
   def cat_name(self,obj):
      return obj.category.name


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)