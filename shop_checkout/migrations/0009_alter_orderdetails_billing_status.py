# Generated by Django 3.2.6 on 2021-11-18 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_checkout', '0008_alter_orderdetails_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='billing_status',
            field=models.CharField(default='Processing', max_length=70),
        ),
    ]