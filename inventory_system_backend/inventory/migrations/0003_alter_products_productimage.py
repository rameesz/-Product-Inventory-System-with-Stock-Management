# Generated by Django 5.1 on 2024-08-09 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_products_createduser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='ProductImage',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
