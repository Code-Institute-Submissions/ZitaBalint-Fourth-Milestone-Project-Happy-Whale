# Generated by Django 3.2.6 on 2021-08-23 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image_url',
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
    ]
