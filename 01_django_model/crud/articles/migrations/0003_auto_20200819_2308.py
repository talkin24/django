# Generated by Django 3.1 on 2020-08-19 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_aricle_updated_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Aricle',
            new_name='Article',
        ),
    ]
