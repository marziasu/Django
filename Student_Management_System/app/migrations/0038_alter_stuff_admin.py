# Generated by Django 4.2.7 on 2023-12-08 01:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_alter_stuff_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuff',
            name='admin',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
