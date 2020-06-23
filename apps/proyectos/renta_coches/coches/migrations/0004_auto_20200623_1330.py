# Generated by Django 3.0.3 on 2020-06-23 18:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('coches', '0003_auto_20200623_1324'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coches',
            options={'verbose_name': 'Coche', 'verbose_name_plural': 'Coches'},
        ),
        migrations.RemoveField(
            model_name='coches',
            name='image',
        ),
        migrations.AddField(
            model_name='coches',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='projects/renta_coches/coches/',
                                    verbose_name='Imagen'),
        ),
    ]