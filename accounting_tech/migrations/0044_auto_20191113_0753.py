# Generated by Django 2.1.7 on 2019-11-13 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_tech', '0043_auto_20191113_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportrequesttorepair',
            name='fio_executor',
            field=models.CharField(blank=True, max_length=150, verbose_name='ФИО исполнителя'),
        ),
        migrations.AddField(
            model_name='reportrequesttorepair',
            name='post',
            field=models.CharField(blank=True, max_length=100, verbose_name='Должность исполнителя'),
        ),
        migrations.AddField(
            model_name='reportrequesttorepair',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]
