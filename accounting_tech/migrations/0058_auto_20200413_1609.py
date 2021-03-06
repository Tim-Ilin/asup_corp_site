# Generated by Django 2.2.12 on 2020-04-13 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_tech', '0057_requesttorepair_is_repaired'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportrequesttorepair',
            name='time_field',
        ),
        migrations.AlterField(
            model_name='reportrequesttorepair',
            name='request_to_repair',
            field=models.ForeignKey(limit_choices_to={'is_repaired': False}, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting_tech.RequestToRepair', verbose_name='Заявитель'),
        ),
        migrations.AlterField(
            model_name='requesttorepair',
            name='is_repaired',
            field=models.BooleanField(default=False, verbose_name='выполнено'),
        ),
    ]
