# Generated by Django 3.2.6 on 2021-09-10 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20210910_0238'),
        ('shop_checkout', '0007_orderdetails_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='profiles.userprofile'),
        ),
    ]
