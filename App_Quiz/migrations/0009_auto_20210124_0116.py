# Generated by Django 3.1.5 on 2021-01-23 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Quiz', '0008_quiz_quizquestion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizquestion',
            name='category',
        ),
        migrations.RemoveField(
            model_name='quizquestion',
            name='quiz',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.DeleteModel(
            name='QuizQuestion',
        ),
    ]
