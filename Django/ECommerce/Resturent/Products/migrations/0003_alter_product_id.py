# Generated by Django 4.2.7 on 2023-12-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
