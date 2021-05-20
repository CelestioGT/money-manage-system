# Generated by Django 2.0.7 on 2021-05-11 23:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_rename_redcord_record'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='name',
        ),
        migrations.AddField(
            model_name='record',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='วันที่'),
        ),
        migrations.AlterField(
            model_name='record',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]