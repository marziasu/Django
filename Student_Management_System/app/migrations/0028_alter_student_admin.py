# Generated by Django 4.2.7 on 2023-12-07 00:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_stuff_admin_alter_student_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
