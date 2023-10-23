from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)  # Поле для заголовка статьи
    content = models.TextField()  # Поле для содержания статьи
    objects = models.Manager()
    def __str__(self):
        return self.title
