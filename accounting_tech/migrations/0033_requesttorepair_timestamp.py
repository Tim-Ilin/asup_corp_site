# Generated by Django 2.1.7 on 2019-04-12 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_tech', '0032_auto_20190412_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='requesttorepair',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, verbose_name='Время создания заявки'),
        ),
    ]