# Generated by Django 5.0.7 on 2024-07-22 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]