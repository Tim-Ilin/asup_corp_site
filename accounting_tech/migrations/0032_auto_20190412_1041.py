# Generated by Django 2.1.7 on 2019-04-12 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_tech', '0031_requesttorepair_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requesttorepair',
            name='location',
            field=models.CharField(max_length=100, verbose_name='Местонахождение'),
        ),
    ]
