# Generated by Django 3.1.5 on 2021-01-20 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App_Article', '0002_auto_20210119_1336'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-created_at',)},
        ),
        migrations.CreateModel(
            name='Unlike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unliked_date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='total_unlikes', to='App_Article.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_unliked_articles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='total_likes', to='App_Article.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_liked_articles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]