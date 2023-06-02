from django.contrib import admin
from eshop.models import ProductList, Category
# Register your models here.


class ProductListAdmin(admin.ModelAdmin):
    list_display = ('title', 'price',
                    'description', 'slug', 'photo')
    
class CategoryListAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo')

admin.site.register(ProductList, ProductListAdmin)
admin.site.register(Category, CategoryListAdmin)
