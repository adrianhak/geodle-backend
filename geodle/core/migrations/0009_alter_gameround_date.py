# Generated by Django 4.0.5 on 2022-06-03 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_gameround_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameround',
            name='date',
            field=models.DateTimeField(primary_key=True, serialize=False),
        ),
    ]