# Generated by Django 3.1.5 on 2021-01-22 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Article', '0007_auto_20210121_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='articles'),
        ),
    ]