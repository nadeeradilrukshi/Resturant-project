# Generated by Django 3.2.23 on 2023-12-07 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
