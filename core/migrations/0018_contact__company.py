# Generated by Django 3.0.6 on 2020-06-04 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='_company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Company'),
        ),
    ]
