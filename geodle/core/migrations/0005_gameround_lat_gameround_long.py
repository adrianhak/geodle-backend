# Generated by Django 4.0.5 on 2022-06-03 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_location_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameround',
            name='lat',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gameround',
            name='long',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]