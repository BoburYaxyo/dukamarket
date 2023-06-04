# Generated by Django 3.2.7 on 2023-06-03 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0019_auto_20230603_0722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=150)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('street_address', models.CharField(max_length=100)),
                ('home_place_number', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('town_or_city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('post_code', models.CharField(max_length=100)),
                ('email_adress', models.EmailField(max_length=100)),
                ('ship_different', models.BooleanField(default=False)),
            ],
        ),
    ]
