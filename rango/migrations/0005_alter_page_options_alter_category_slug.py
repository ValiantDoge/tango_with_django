# Generated by Django 4.0.5 on 2022-06-27 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_alter_category_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name_plural': 'Pages'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
