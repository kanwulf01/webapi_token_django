# Generated by Django 3.0.3 on 2020-03-12 03:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserDefault', '0017_auto_20200312_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariomedico',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
