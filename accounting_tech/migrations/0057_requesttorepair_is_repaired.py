# Generated by Django 2.1.7 on 2020-04-09 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_tech', '0056_auto_20200409_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='requesttorepair',
            name='is_repaired',
            field=models.BooleanField(default=False),
        ),
    ]