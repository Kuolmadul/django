# Generated by Django 3.2.12 on 2024-02-27 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='phone',
        ),
    ]