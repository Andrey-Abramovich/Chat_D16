from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='никнейм')
    first_name = models.CharField(max_length=24, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=24, blank=True, null=True, verbose_name='Фамилия')
    birthday = models.DateField(blank=True, verbose_name='дата рождения')
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d', blank=True, null=True, verbose_name='аватарка')
    email = models.EmailField(blank=True)


    def __str__(self):
        return self.user