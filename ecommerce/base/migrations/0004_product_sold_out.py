# Generated by Django 5.1.1 on 2024-10-10 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_cart_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sold_out',
            field=models.BooleanField(default=False),
        ),
    ]
