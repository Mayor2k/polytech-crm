# Generated by Django 3.0.6 on 2020-05-29 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('phone_number', models.CharField(blank=True, max_length=15, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Почта')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='ФИО клиента')),
                ('title', models.CharField(default='Лид №<built-in function id>', max_length=50, verbose_name='Название лида')),
                ('phone_number', models.CharField(blank=True, max_length=15, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Почта')),
                ('opportunity', models.FloatField(default=0)),
                ('opportunity_currency', models.PositiveSmallIntegerField(default=1)),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Contact')),
            ],
        ),
    ]