# Generated by Django 3.1.5 on 2021-01-12 09:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("vocabs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="GeoNamesPlace",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "legacy_id",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="Legacy ID"
                    ),
                ),
                (
                    "gn_id",
                    models.IntegerField(
                        blank=True,
                        help_text="GeoNames ID",
                        null=True,
                        verbose_name="GeoNames ID",
                    ),
                ),
                (
                    "gn_name",
                    models.CharField(
                        blank=True,
                        help_text="Name",
                        max_length=250,
                        verbose_name="Name",
                    ),
                ),
                (
                    "gn_lat",
                    models.FloatField(
                        blank=True,
                        help_text="Latitude",
                        null=True,
                        verbose_name="latitude",
                    ),
                ),
                (
                    "gn_long",
                    models.FloatField(
                        blank=True,
                        help_text="Longitude",
                        null=True,
                        verbose_name="longitude",
                    ),
                ),
                (
                    "gn_feature_class",
                    models.CharField(
                        blank=True,
                        help_text="Feature Class",
                        max_length=250,
                        null=True,
                        verbose_name="Feature Class",
                    ),
                ),
                (
                    "gn_feature_code",
                    models.CharField(
                        blank=True,
                        help_text="Feature Code",
                        max_length=250,
                        null=True,
                        verbose_name="Feature Code",
                    ),
                ),
                (
                    "gn_country_code",
                    models.CharField(
                        blank=True,
                        help_text="Country Code",
                        max_length=250,
                        null=True,
                        verbose_name="Country Code",
                    ),
                ),
                (
                    "gn_cc2",
                    models.CharField(
                        blank=True,
                        help_text="Alternate Country Codes",
                        max_length=250,
                        null=True,
                        verbose_name="Alternate Country Codes",
                    ),
                ),
                (
                    "gn_population",
                    models.IntegerField(
                        blank=True,
                        help_text="Population",
                        null=True,
                        verbose_name="Population",
                    ),
                ),
                (
                    "gn_elevation",
                    models.IntegerField(
                        blank=True,
                        help_text="Elevation (m)",
                        null=True,
                        verbose_name="Elevation (m)",
                    ),
                ),
                (
                    "gn_modification_date",
                    models.DateField(
                        blank=True,
                        help_text="Modification Date",
                        null=True,
                        verbose_name="Modifcation Date",
                    ),
                ),
                (
                    "orig_data_csv",
                    models.TextField(
                        blank=True, null=True, verbose_name="The original data"
                    ),
                ),
                (
                    "gn_feature",
                    models.ForeignKey(
                        blank=True,
                        help_text="The Place's Feature Code as SKOS",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="vocabs.skosconcept",
                        verbose_name="Feature Code as SKOS",
                    ),
                ),
            ],
            options={
                "verbose_name": "GeoNamesPlace",
                "ordering": ["gn_name"],
            },
        ),
    ]
