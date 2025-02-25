# Generated by Django 4.2.7 on 2023-11-28 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_student_permanent_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(default='default'),
        ),
        migrations.AddField(
            model_name='student',
            name='session_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='app.session'),
        ),
    ]
