# Generated by Django 3.1.7 on 2021-03-11 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0002_auto_20210311_0218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='pet_name',
            new_name='nickname',
        ),
    ]
