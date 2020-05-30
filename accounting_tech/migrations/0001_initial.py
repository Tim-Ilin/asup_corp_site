# Generated by Django 2.1.7 on 2019-03-15 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50, verbose_name='Должность')),
                ('state', models.CharField(max_length=50, verbose_name='Состояние')),
            ],
            options={
                'verbose_name': 'Работники',
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('date_bought', models.DateField()),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting_tech.Employees')),
            ],
        ),
        migrations.CreateModel(
            name='Move_tech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_issue', models.DateField()),
                ('date_of_back', models.DateField()),
                ('equipment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting_tech.Equipment')),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting_tech.Employees')),
            ],
        ),
    ]
