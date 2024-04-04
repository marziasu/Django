# Generated by Django 4.2.7 on 2023-12-06 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_course_department_id_course_stuff_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='department_id',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.DO_NOTHING, to='app.department'),
        ),
        migrations.AlterField(
            model_name='course',
            name='stuff_id',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.DO_NOTHING, to='app.stuff'),
        ),
    ]
