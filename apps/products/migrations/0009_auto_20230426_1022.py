# Generated by Django 3.2.4 on 2023-04-26 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_cart_wishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='product',
            new_name='products',
        ),
        migrations.RenameField(
            model_name='wishlist',
            old_name='product',
            new_name='products',
        ),
    ]
