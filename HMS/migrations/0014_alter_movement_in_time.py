# Generated by Django 4.0.5 on 2022-07-18 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0013_alter_movement_in_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='in_time',
            field=models.DateTimeField(null=True),
        ),
    ]
