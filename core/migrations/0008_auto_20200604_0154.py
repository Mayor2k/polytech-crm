# Generated by Django 3.0.6 on 2020-06-03 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200604_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='_stage_id',
            field=models.IntegerField(default=1, verbose_name='Стадия лида'),
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('crmentity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.CrmEntity')),
                ('_title', models.CharField(default='Сделка №<built-in function id>', max_length=50, verbose_name='Название сделки')),
                ('_stage_id', models.IntegerField(default=1, verbose_name='Стадия сделки')),
                ('_lead', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Lead')),
            ],
            bases=('core.crmentity',),
        ),
    ]
