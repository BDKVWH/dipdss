# Generated by Django 3.1.7 on 2021-04-07 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dss', '0004_auto_20210331_0443'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultmodel',
            name='gd',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultmodel',
            name='igd',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultmodel',
            name='spread',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
