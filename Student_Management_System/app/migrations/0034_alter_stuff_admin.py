# Generated by Django 4.2.7 on 2023-12-07 00:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_alter_student_department_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuff',
            name='admin',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
