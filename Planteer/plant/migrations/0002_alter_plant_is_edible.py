# Generated by Django 5.0.6 on 2024-11-08 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='is_edible',
            field=models.BooleanField(default=False),
        ),
    ]