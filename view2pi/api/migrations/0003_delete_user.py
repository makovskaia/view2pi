# Generated by Django 3.2.7 on 2021-09-08 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210907_1928'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]