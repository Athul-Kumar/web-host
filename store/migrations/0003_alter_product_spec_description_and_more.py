# Generated by Django 4.1.1 on 2022-10-04 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_spec_description_product_spec_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='spec_description',
            field=models.TextField(blank=True, max_length=555, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='spec_title',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]