# Generated by Django 3.1.7 on 2021-03-11 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Info',
            new_name='Cat',
        ),
    ]
