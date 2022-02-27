# Generated by Django 3.2 on 2022-02-24 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(blank=True, choices=[('1', 'Male'), ('2', 'Female'), ('2', 'Non Binary')], max_length=254, null=True),
        ),
    ]