# Generated by Django 4.2.7 on 2023-12-04 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_stuff_leave'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stuff_leave',
            old_name='data',
            new_name='date',
        ),
    ]
