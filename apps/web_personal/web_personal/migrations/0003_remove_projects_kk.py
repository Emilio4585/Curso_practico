# Generated by Django 3.0.3 on 2020-06-17 19:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('web_personal', '0002_projects_kk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='kk',
        ),
    ]