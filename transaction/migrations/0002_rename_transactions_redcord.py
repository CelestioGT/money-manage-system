# Generated by Django 3.2.1 on 2021-05-05 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='transactions',
            new_name='redcord',
        ),
    ]