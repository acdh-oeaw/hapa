# Generated by Django 3.1.6 on 2021-02-09 10:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("archiv", "0005_hapaplacename_etymology"),
    ]

    operations = [
        migrations.AddField(
            model_name="hapaplacename",
            name="syntax",
            field=ckeditor.fields.RichTextField(
                blank=True,
                help_text="Besprechung der Syntax des Ortsnamens",
                null=True,
                verbose_name="Syntax",
            ),
        ),
    ]
