# Generated by Django 3.0.6 on 2020-06-04 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200604_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crmentity',
            name='_contact',
        ),
    ]