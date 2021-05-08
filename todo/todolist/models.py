from django.db import models
from django.utils import timezone

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Описание')
    choice_priority = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )
    priority = models.CharField('Приоритет', max_length=1, choices=choice_priority)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Список дел'
        verbose_name_plural = 'Список дел'