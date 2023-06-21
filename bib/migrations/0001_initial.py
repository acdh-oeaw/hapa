# Generated by Django 2.0.2 on 2018-07-05 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZotItem',
            fields=[
                ('zot_key', models.CharField(help_text='The Zotero Item Key', max_length=20, primary_key=True, serialize=False, verbose_name='key')),
                ('zot_creator', models.TextField(blank=True, help_text="Stores all information from zoteros 'creators' field.", verbose_name='creators')),
                ('zot_date', models.TextField(blank=True, help_text="Stores all information from zoteros 'date' field.", verbose_name='date')),
                ('zot_item_type', models.TextField(blank=True, help_text="Stores all information from zoteros 'itemType' field.", verbose_name='itemType')),
                ('zot_title', models.TextField(blank=True, help_text="Stores all information from zoteros 'title' field.", verbose_name='title')),
                ('zot_pub_title', models.TextField(blank=True, help_text="Stores all information from zoteros 'publicationTitle' field.", verbose_name='publicationTitle')),
                ('date_modified', models.DateTimeField(blank=True, help_text="Stores all information from zoteros 'publicationTitle' field.", null=True, verbose_name='dateModified')),
                ('zot_pages', models.TextField(blank=True, help_text="Stores all information from zoteros 'pages' field.", verbose_name='pages')),
                ('zot_version', models.IntegerField(blank=True, help_text="Stores all information from zoteros 'pages' field.", null=True, verbose_name='version')),
                ('zot_html_link', models.CharField(blank=True, help_text="Stores all information from zoteros 'selflink' field.", max_length=500, verbose_name='selflink html')),
                ('zot_api_link', models.CharField(blank=True, help_text='Stores all information from zoteros self api link field.', max_length=500, verbose_name='selflink api')),
                ('zot_bibtex', models.TextField(blank=True, help_text="Stores the item's bibtex representation.", verbose_name='bibtex')),
            ],
            options={
                'ordering': ['-zot_version'],
            },
        ),
    ]