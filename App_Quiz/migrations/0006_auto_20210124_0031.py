# Generated by Django 3.1.5 on 2021-01-23 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Quiz', '0005_auto_20210124_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizquestion',
            name='answer',
            field=models.CharField(choices=[('A', 'option 1'), ('B', 'option 2'), ('C', 'option 3'), ('D', 'option 4')], default=('A', 'option 1'), max_length=2),
        ),
    ]