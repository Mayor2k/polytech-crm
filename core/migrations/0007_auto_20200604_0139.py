# Generated by Django 3.0.6 on 2020-06-03 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_lead_asd'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crmentity',
            old_name='name',
            new_name='_name',
        ),
    ]