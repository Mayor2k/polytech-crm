# Generated by Django 3.0.6 on 2020-06-04 16:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20200604_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
    ]
