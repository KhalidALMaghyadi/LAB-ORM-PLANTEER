# Generated by Django 5.0.6 on 2024-11-10 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0002_alter_plant_is_edible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='is_edible',
            field=models.BooleanField(),
        ),
    ]
