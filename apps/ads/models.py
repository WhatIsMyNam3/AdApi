from django.db import models


class Ad(models.Model):
    title = models.CharField(
        verbose_name='Заголовок объявления',
        max_length=255
    )
    ad_id = models.PositiveIntegerField(
        verbose_name='ID объявления',
        unique=True
    )
    author = models.CharField(
        verbose_name='Автор объявления',
        max_length=100
    )
    views = models.PositiveIntegerField(
        verbose_name='Количество просмотров'
    )
    position = models.PositiveSmallIntegerField(
        verbose_name='Позиция объявления'
    )

    def __str__(self) -> str:
        return self.title
