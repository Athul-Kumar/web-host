# Generated by Django 4.1.1 on 2022-10-02 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_category_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]