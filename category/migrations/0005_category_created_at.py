# Generated by Django 4.1.1 on 2022-11-04 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_category_category_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
