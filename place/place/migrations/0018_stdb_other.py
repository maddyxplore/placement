# Generated by Django 3.0.3 on 2020-03-22 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0017_auto_20200314_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='stdb',
            name='other',
            field=models.CharField(default='nill', max_length=1000),
            preserve_default=False,
        ),
    ]