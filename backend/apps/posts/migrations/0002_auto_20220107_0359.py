# Generated by Django 3.2.7 on 2022-01-07 03:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dislike',
            options={'verbose_name': 'Дизлайк', 'verbose_name_plural': 'Дизлайки'},
        ),
        migrations.AlterModelOptions(
            name='like',
            options={'verbose_name': 'Лайк', 'verbose_name_plural': 'Лайки'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='like_raing',
            new_name='like_rating',
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='posts.post', verbose_name='Пост'),
        ),
        migrations.AlterField(
            model_name='like',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
