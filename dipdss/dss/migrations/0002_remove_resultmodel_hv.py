# Generated by Django 3.1.7 on 2021-03-26 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dss', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultmodel',
            name='hv',
        ),
    ]