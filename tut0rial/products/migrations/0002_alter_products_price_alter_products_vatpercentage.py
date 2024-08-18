# Generated by Django 5.1 on 2024-08-17 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="price",
            field=models.FloatField(db_column="bookprice"),
        ),
        migrations.AlterField(
            model_name="products",
            name="vatpercentage",
            field=models.FloatField(db_column="bookvatpercentage"),
        ),
    ]
