from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    likes_count = models.IntegerField(verbose_name='Кол-во лайков', default=0)
    description = models.CharField(verbose_name='Описание', null=False, max_length=200)
    image = models.ImageField(verbose_name='Фото', null=True, blank=True, upload_to='posts')
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='posts', null=False, blank=False,
                               on_delete=models.CASCADE)
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        null=False,
        default=False
    )


class Comment(models.Model):
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='comments', null=False, blank=False,
                               on_delete=models.CASCADE)
    post = models.ForeignKey(verbose_name='Публикация', to='posts.Post', related_name='comments', null=False,
                             blank=False,
                             on_delete=models.CASCADE)
    text = models.CharField(verbose_name='Комментарий', null=False, blank=False, max_length=200)