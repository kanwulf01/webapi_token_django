# Generated by Django 3.0.3 on 2020-03-11 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserDefault', '0008_auto_20200311_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='empleado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empleados', to='UserDefault.Empleado'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to=settings.AUTH_USER_MODEL),
        ),
    ]
