# Generated by Django 3.2.3 on 2021-05-21 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0015_auto_20210521_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='lesson_time',
            field=models.DateTimeField(verbose_name='Дата занятия'),
        ),
    ]
