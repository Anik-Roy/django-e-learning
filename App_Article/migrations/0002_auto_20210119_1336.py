# Generated by Django 3.1.5 on 2021-01-19 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
