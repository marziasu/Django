# Generated by Django 4.2.7 on 2023-12-07 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_alter_stuff_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.department'),
        ),
    ]
