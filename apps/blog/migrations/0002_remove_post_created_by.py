# Generated by Django 3.2.7 on 2023-05-30 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_by',
        ),
    ]
