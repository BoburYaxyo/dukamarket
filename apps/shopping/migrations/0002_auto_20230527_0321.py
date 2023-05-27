# Generated by Django 3.2.7 on 2023-05-27 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='shopping.colors'),
            preserve_default=False,
        ),
    ]