# Generated by Django 4.1.7 on 2023-05-28 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0002_category_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlist',
            name='full_description',
            field=models.TextField(null=True, verbose_name='Подробное описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(upload_to='images/shop_icons', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='description',
            field=models.TextField(null=True, verbose_name='Краткое описание'),
        ),
    ]
