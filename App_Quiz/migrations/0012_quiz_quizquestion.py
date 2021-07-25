# Generated by Django 3.1.5 on 2021-01-23 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('App_Article', '0008_auto_20210122_0654'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App_Quiz', '0011_auto_20210124_0128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_quizes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_question', models.CharField(max_length=500)),
                ('option1', models.CharField(max_length=500)),
                ('option2', models.CharField(max_length=500)),
                ('option3', models.CharField(max_length=500)),
                ('option4', models.CharField(max_length=500)),
                ('answer', models.CharField(choices=[('A', 'option 1'), ('B', 'option 2'), ('C', 'option 3'), ('D', 'option 4')], default=('A', 'option 1'), max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_quiz_questions', to='App_Article.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_quiz_questions', to=settings.AUTH_USER_MODEL)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_questions', to='App_Quiz.quiz')),
            ],
        ),
    ]