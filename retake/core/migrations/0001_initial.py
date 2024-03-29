# Generated by Django 3.2.8 on 2021-10-22 01:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('category', models.CharField(max_length=255, verbose_name='categoria')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
                ('number', models.CharField(max_length=255, verbose_name='número')),
                ('class_name', models.CharField(max_length=255, verbose_name='classe')),
                ('subject', models.CharField(max_length=255, verbose_name='assunto')),
                ('judge', models.CharField(max_length=255, verbose_name='juíz')),
                ('parts', models.ManyToManyField(to='core.Part', verbose_name='partes')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
