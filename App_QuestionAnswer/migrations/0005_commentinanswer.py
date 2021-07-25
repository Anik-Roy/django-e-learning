# Generated by Django 3.1.5 on 2021-01-21 23:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App_QuestionAnswer', '0004_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentInAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_comments', to='App_QuestionAnswer.answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments_in_answer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
