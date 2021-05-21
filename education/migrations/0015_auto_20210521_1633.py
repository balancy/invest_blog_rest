# Generated by Django 3.2.3 on 2021-05-21 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0014_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='responsible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='courses', to='education.mentor', verbose_name='Отвественный'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lessons', to='education.mentor', verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='education.lesson', verbose_name='Занятие'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='education.student', verbose_name='Студент'),
        ),
    ]
