# Generated by Django 4.0.4 on 2022-05-24 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='type',
            field=models.IntegerField(choices=[(0, 'fundacja'), (1, 'organizacja pozarządowa'), (2, 'zbiórka lokalna')], default=0),
        ),
    ]
