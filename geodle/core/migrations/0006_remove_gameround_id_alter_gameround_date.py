# Generated by Django 4.0.5 on 2022-06-03 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_gameround_lat_gameround_long'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameround',
            name='id',
        ),
        migrations.AlterField(
            model_name='gameround',
            name='date',
            field=models.DateField(auto_now_add=True, primary_key=True, serialize=False),
        ),
    ]
