# Generated by Django 3.2.6 on 2021-08-22 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210822_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_slug',
            new_name='category_slug',
        ),
    ]
