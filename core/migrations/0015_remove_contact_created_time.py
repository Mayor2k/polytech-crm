# Generated by Django 3.0.6 on 2020-06-04 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_contact_created_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='created_time',
        ),
    ]