# Generated by Django 3.0.3 on 2020-03-07 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_auto_20200307_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='slogin',
            name='phone_number',
            field=models.CharField(default=0, max_length=30),

        ),
        migrations.AddField(
            model_name='slogin',
            name='tenth',
            field=models.CharField(default=0, max_length=30),

        ),
        migrations.AddField(
            model_name='slogin',
            name='lang',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
