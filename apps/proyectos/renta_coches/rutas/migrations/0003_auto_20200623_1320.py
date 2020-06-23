# Generated by Django 3.0.3 on 2020-06-23 18:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('rutas', '0002_auto_20200623_1255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ruta',
            old_name='name',
            new_name='nombre',
        ),
        migrations.AlterField(
            model_name='ruta',
            name='descripcion',
            field=models.TextField(blank=True, default=None, max_length=50, null=True),
        ),
    ]