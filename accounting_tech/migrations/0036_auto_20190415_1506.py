# Generated by Django 2.1.7 on 2019-04-15 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_tech', '0035_auto_20190415_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requesttorepair',
            name='description_failure',
            field=models.TextField(blank=True, max_length=200, verbose_name='Краткое описание неисправности'),
        ),
    ]
