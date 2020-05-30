# Generated by Django 2.1.7 on 2019-04-03 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_tech', '0009_auto_20190403_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='ip_address',
            field=models.GenericIPAddressField(null=True, verbose_name='IP адрес'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='mac_address',
            field=models.CharField(blank=True, max_length=100, verbose_name='MAC адрес'),
        ),
    ]