# Generated by Django 4.2.1 on 2023-12-15 20:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PropertyModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=30, verbose_name="Title")),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=9, verbose_name="Price"
                    ),
                ),
                ("location", models.CharField(max_length=30, verbose_name="Location")),
                (
                    "property_type",
                    models.CharField(
                        choices=[("house", "house"), ("apartment", "apartment")],
                        max_length=20,
                        verbose_name="Property Type",
                    ),
                ),
                ("bedrooms", models.IntegerField(verbose_name="Bedrooms")),
                ("bathrooms", models.IntegerField(verbose_name="Bathrooms")),
                ("square_feet", models.IntegerField(verbose_name="Square Feet")),
                (
                    "available",
                    models.BooleanField(default=True, verbose_name="Available"),
                ),
            ],
            options={
                "verbose_name": "Property",
                "verbose_name_plural": "Properties",
                "ordering": ["title"],
            },
        ),
    ]
