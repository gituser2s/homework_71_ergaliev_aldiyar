# Generated by Django 4.1.7 on 2023-04-20 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество лайков'),
        ),
    ]
