# Generated by Django 4.1.1 on 2022-10-16 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='amount_id',
        ),
    ]
