# Generated by Django 3.0.3 on 2020-03-11 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserDefault', '0004_auto_20200311_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='empleado',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empleado', to='UserDefault.Empleado'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
