# Generated by Django 3.2.6 on 2021-08-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_item_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='display_name',
        ),
        migrations.AddField(
            model_name='category',
            name='category_slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]
