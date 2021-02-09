# Generated by Django 3.1.6 on 2021-02-09 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0002_auto_20210202_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='hapaplacename',
            name='historic',
            field=models.BooleanField(default=False, help_text='Historischer Ort bedeutet es gibt diesen Ort heute nicht mehr', verbose_name='Historischer Ort'),
        ),
    ]
