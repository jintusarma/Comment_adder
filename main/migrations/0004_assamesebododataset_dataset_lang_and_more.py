# Generated by Django 4.0.6 on 2023-06-18 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_assamesebododataset_assameseenglishdataset_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assamesebododataset',
            name='dataset_lang',
            field=models.CharField(blank=True, default='ab', max_length=100, null=True, verbose_name='Dataset Language'),
        ),
        migrations.AddField(
            model_name='assameseenglishdataset',
            name='dataset_lang',
            field=models.CharField(blank=True, default='ab', max_length=100, null=True, verbose_name='Dataset Language'),
        ),
        migrations.AddField(
            model_name='bodoenglishdataset',
            name='dataset_lang',
            field=models.CharField(blank=True, default='ab', max_length=100, null=True, verbose_name='Dataset Language'),
        ),
    ]