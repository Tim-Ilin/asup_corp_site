# Generated by Django 2.1.7 on 2019-11-12 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_tech', '0041_auto_20191112_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportrequesttorepair',
            name='request_to_repair',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting_tech.RequestToRepair', verbose_name='Заявитель'),
        ),
    ]
