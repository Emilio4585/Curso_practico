# Generated by Django 3.0.3 on 2020-06-23 17:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('coches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coches',
            name='categoria',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='coches',
            name='descripcion',
            field=models.TextField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='coches',
            name='numero',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='coches',
            name='tipo',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]