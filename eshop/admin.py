from django.contrib import admin
from eshop.models import ProductList
# Register your models here.


class ProductListAdmin(admin.ModelAdmin):
    list_display = ('title', 'price',
                    'description', 'slug', 'photo')


admin.site.register(ProductList, ProductListAdmin)
