# Generated by Django 3.0.3 on 2020-06-17 19:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('web_personal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='kk',
            field=models.IntegerField(default=0),
        ),
    ]
