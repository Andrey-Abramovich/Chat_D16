from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    # ROLE = (
    #     ("tank", "танк"),
    #     ("heal", "хил"),
    #     ("dd", "ДД"),
    #     ("seller", "торговец"),
    #     ("gm", "гилдмастер"),
    #     ("quest", "квестгивер"),
    #     ("blacksmith", "кузнец"),
    #     ("skinner", "кожевник"),
    #     ("potion", "зельевар"),
    #     ("spell", "мастер заклинаний")
    # )
    title = models.CharField(max_length=128, verbose_name="Заголовок")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    roles = models.ForeignKey("Category", on_delete=models.CASCADE, blank=True)
    upload = models.FileField(upload_to='uploads/')

    def __str__(self):
        return '{}'.format(self.title)


class Category(models.Model):
    name = models.CharField(max_length=28, unique=True, verbose_name='Название')

    def __str__(self):
        return '{}'.format(self.name)


class Respond(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=False)
    dateCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.text)