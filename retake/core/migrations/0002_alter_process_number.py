# Generated by Django 3.2.8 on 2021-10-22 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='number',
            field=models.CharField(max_length=255, unique=True, verbose_name='número'),
        ),
    ]
