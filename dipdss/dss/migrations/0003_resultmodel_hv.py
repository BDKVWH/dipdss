# Generated by Django 3.1.7 on 2021-03-26 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dss', '0002_remove_resultmodel_hv'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultmodel',
            name='hv',
            field=models.FloatField(blank=True, null=True),
        ),
    ]