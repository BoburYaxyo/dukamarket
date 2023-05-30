# Generated by Django 3.2.7 on 2023-05-30 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_remove_post_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_by',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='auth.user'),
            preserve_default=False,
        ),
    ]