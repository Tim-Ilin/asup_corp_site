# Generated by Django 2.1.7 on 2019-12-18 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_tech', '0050_auto_20191217_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acquisition',
            name='room',
        ),
        migrations.AlterField(
            model_name='employees',
            name='pin_code',
            field=models.IntegerField(verbose_name='Пинкод'),
        ),
    ]