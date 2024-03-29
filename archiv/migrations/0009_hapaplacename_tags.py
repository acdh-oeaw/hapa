# Generated by Django 3.1.6 on 2021-02-26 19:04

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("taggit", "0003_taggeditem_add_unique_index"),
        ("archiv", "0008_hapaplacename_fuzzy_geom"),
    ]

    operations = [
        migrations.AddField(
            model_name="hapaplacename",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
