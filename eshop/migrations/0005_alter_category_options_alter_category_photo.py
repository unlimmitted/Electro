# Generated by Django 4.1.7 on 2023-06-06 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0004_usercartlist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категории', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(upload_to='shop_icons', verbose_name='Фото'),
        ),
    ]
