# Generated by Django 2.1.7 on 2019-11-12 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_tech', '0037_requesttorepair_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requesttorepair',
            name='report',
        ),
    ]
