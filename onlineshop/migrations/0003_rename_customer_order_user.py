# Generated by Django 4.0.1 on 2022-04-09 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0002_rename_user_order_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='user',
        ),
    ]
