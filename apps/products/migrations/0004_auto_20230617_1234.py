# Generated by Django 3.2.7 on 2023-06-17 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20230617_0353'),
        ('products', '0003_auto_20230617_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='cartproducts', to='shopping.Product'),
        ),
    ]