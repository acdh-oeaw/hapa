# Generated by Django 3.1.6 on 2021-12-09 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0013_hapaplacename_alternative_names'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hapabeleg',
            old_name='page',
            new_name='page_nr',
        ),
    ]