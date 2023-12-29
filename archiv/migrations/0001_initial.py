# Generated by Django 3.1.5 on 2021-01-25 10:49

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("gn_places", "0001_initial"),
        ("bib", "0001_initial"),
        ("vocabs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HapaBeleg",
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
                    "text",
                    models.TextField(
                        blank=True,
                        help_text="ausgewähltes Quellenzitaten",
                        null=True,
                        verbose_name="Textauszug",
                    ),
                ),
                (
                    "page",
                    models.CharField(
                        blank=True,
                        help_text="z.B. S. 44-46",
                        max_length=250,
                        verbose_name="genaue Stelle",
                    ),
                ),
                (
                    "short_quote",
                    models.CharField(
                        blank=True,
                        help_text="wird automatisch aus verknüpftem Zotero Eintrag übernommen",
                        max_length=250,
                        verbose_name="Kurzzitat",
                    ),
                ),
                (
                    "full_quote",
                    models.TextField(
                        blank=True,
                        help_text="wird automatisch aus verknüpftem Zotero Eintrag übernommen",
                        null=True,
                        verbose_name="Vollzitat",
                    ),
                ),
                (
                    "time_of_origin_start",
                    models.IntegerField(
                        blank=True,
                        help_text="Jahreszahl, z.B. 800 für 9. Jh",
                        null=True,
                        verbose_name="Zeitliche Einordnung (Beginn)",
                    ),
                ),
                (
                    "time_of_origin_end",
                    models.IntegerField(
                        blank=True,
                        help_text="Jahreszahl, z.B. 899 für 9. Jh",
                        null=True,
                        verbose_name="Zeitliche Einordnung (Ende)",
                    ),
                ),
                (
                    "orig_data_csv",
                    models.TextField(
                        blank=True, null=True, verbose_name="The original data"
                    ),
                ),
                (
                    "zotero_id",
                    models.ForeignKey(
                        blank=True,
                        help_text="Zoteroeintrag",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="rvn_hapabeleg_zotero_id_zotitem",
                        to="bib.zotitem",
                        verbose_name="Zoteroeintrag",
                    ),
                ),
            ],
            options={
                "verbose_name": "Beleg",
                "ordering": ["short_quote"],
            },
        ),
        migrations.CreateModel(
            name="HapaPlaceName",
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
                    "name",
                    models.CharField(
                        blank=True,
                        help_text="Standardisierte Namensansetzung",
                        max_length=250,
                        verbose_name="Name",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Besprechung der Etymologie und Wortbildung des Ortsnamens",
                        null=True,
                        verbose_name="Etymologie und Wortbildung",
                    ),
                ),
                (
                    "lat",
                    models.FloatField(
                        blank=True,
                        help_text="Latitude",
                        null=True,
                        verbose_name="Breitengrad",
                    ),
                ),
                (
                    "long",
                    models.FloatField(
                        blank=True,
                        help_text="Longitude",
                        null=True,
                        verbose_name="Längengrad",
                    ),
                ),
                (
                    "point",
                    django.contrib.gis.db.models.fields.PointField(
                        blank=True,
                        help_text="Koordinaten (wird automatische aus den Angaben von Beiten- und Längengrad befüllt)",
                        null=True,
                        srid=4326,
                        verbose_name="Koordinaten",
                    ),
                ),
                (
                    "orig_data_csv",
                    models.TextField(
                        blank=True, null=True, verbose_name="The original data"
                    ),
                ),
                (
                    "adm_unit",
                    models.ForeignKey(
                        blank=True,
                        help_text="Angabe der politisch-administrativen Verortung in Region, Bezirk, Kreis, usw.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="rvn_hapaplacename_adm_unit_skosconcept",
                        to="vocabs.skosconcept",
                        verbose_name="Administrative Einheit",
                    ),
                ),
                (
                    "beleg",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Dokumentation der Belege mit ausgewählten Quellenzitaten",
                        related_name="rvn_hapaplacename_beleg_beleg",
                        to="archiv.HapaBeleg",
                        verbose_name="Beleg",
                    ),
                ),
                (
                    "geonames",
                    models.ForeignKey(
                        blank=True,
                        help_text="Name für Ort in GeoNames",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="rvn_hapaplacename_geonames_geonamesplace",
                        to="gn_places.geonamesplace",
                        verbose_name="GeoNames Eintrag",
                    ),
                ),
                (
                    "orig_sprache",
                    models.ForeignKey(
                        blank=True,
                        help_text="welcher Sprache entstammt der Ortsname",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="rvn_hapaplacename_orig_sprache_skosconcept",
                        to="vocabs.skosconcept",
                        verbose_name="Sprache",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ortsname",
                "ordering": ["name"],
            },
        ),
    ]
