# Generated by Django 3.0.8 on 2020-07-15 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remoterequests', '0005_auto_20200714_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
