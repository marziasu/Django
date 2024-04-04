# Generated by Django 4.2.7 on 2023-12-08 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_semester_course_semester_id_student_semester_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.course')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.semester')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance_Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attendance_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.attendance')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.student')),
            ],
        ),
    ]
