# Generated by Django 4.0.5 on 2022-07-17 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0011_alter_movement_admission_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='mess_cut',
            field=models.BigIntegerField(default=0),
        ),
    ]
