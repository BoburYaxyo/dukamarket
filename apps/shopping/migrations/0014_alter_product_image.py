# Generated by Django 3.2.7 on 2023-05-27 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0013_auto_20230527_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=2, upload_to='images/'),
            preserve_default=False,
        ),
    ]