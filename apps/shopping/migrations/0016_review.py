# Generated by Django 3.2.4 on 2023-04-25 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0015_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('review', models.TextField()),
                ('save_my', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]
