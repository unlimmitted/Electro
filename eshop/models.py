from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    photo = models.ImageField(
        upload_to="images/shop_icons", verbose_name="Фото")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})


class ProductList(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="Название товара", null=True)
    price = models.CharField(
        max_length=255, verbose_name="Цена", null=True)
    description = models.TextField(verbose_name="Краткое описание", null=True)
    full_description = models.TextField(verbose_name="Подробное описание", null=True)
    slug = AutoSlugField(populate_from='title')
    photo = models.ImageField(
        upload_to="images/%Y/%m/%d", verbose_name="Фото")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ('-id',)

class UserCartList(models.Model):
    username = models.CharField(max_length=35, verbose_name='Пользователь')
    product = models.CharField(max_length=255, verbose_name='Товар в коризну')
    quantity = models.IntegerField(verbose_name='Количество', blank=True, null=True)

    def __str__(self):
        return self.username