# Generated by Django 5.1 on 2024-08-08 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='CreatedUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_products', to='inventory.customer_register'),
        ),
    ]
