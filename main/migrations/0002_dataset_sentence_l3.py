# Generated by Django 4.0.6 on 2023-06-08 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='sentence_L3',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]