# Generated by Django 3.2.7 on 2023-05-27 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0015_auto_20230527_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='home',
        ),
    ]