# Generated by Django 3.2.23 on 2023-12-07 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_alter_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='some_default_value', max_length=255),
        ),
    ]
