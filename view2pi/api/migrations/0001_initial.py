# Generated by Django 3.2.7 on 2021-09-05 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.IntegerField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
                ('image_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_from', to='api.image')),
                ('image_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_to', to='api.image')),
            ],
        ),
    ]
