# Generated by Django 3.0.6 on 2020-06-04 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_contact_created_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_name', models.CharField(max_length=50, verbose_name='Название компании')),
                ('_activity', models.CharField(blank=True, max_length=50, verbose_name='Деятельость')),
                ('_email', models.EmailField(max_length=254, verbose_name='email')),
                ('_phone_number', models.CharField(blank=True, max_length=15, verbose_name='Номер телефона')),
                ('_website', models.CharField(blank=True, max_length=100, verbose_name='Сайт')),
                ('_description', models.CharField(blank=True, max_length=100, verbose_name='Компания')),
            ],
        ),
    ]