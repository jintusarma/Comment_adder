# Generated by Django 4.0.6 on 2023-06-08 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssameseDataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Domain')),
                ('sentence_L1', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BodoDataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Domain')),
                ('sentence_L2', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnglishDataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Domain')),
                ('sentence_L3', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
