# Generated by Django 2.1.7 on 2019-12-17 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_tech', '0049_auto_20191217_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='pin_code',
            field=models.IntegerField(),
        ),
    ]