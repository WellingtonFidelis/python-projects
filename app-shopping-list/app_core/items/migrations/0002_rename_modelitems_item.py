# Generated by Django 4.0.3 on 2022-04-09 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ModelItems',
            new_name='Item',
        ),
    ]
