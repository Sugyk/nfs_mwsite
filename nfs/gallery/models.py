from django.db import models


class Brand(models.Model):
    title = models.CharField(verbose_name='Название бренда')
    country = models.CharField(verbose_name='Страна производитель')
    description = models.TextField(null=True, verbose_name='Описание')
    logo = models.ImageField(verbose_name='Логотип')


class Car(models.Model):
    brand = models.ForeignKey(verbose_name='Марка')
    photo = models.ImageField(verbose_name='Фотография авто')
    model = models.CharField(verbose_name='Модель')
    model_year = models.IntegerField(verbose_name='Год выпуска')


class CarNote(models.Model):
    title = models.CharField(null=True, verbose_name='Описание')
    position = models.IntegerField(verbose_name='Позиция текста')
    content = models.TextField(verbose_name='Содержание')


class CarImage(models.Model):
    position = models.IntegerField(verbose_name='Позиция картинки')
    image = models.ImageField(verbose_name='Картинка')
    description = models.CharField(null=True, verbose_name='Описание')
