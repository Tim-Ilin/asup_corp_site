# Generated by Django 2.1.7 on 2019-04-09 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_tech', '0029_auto_20190409_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Наименование'),
        ),
    ]
