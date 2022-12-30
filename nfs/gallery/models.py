from django.db import models


class Brand(models.Model):
    title = models.CharField(verbose_name='Название бренда')
    country = models.CharField(verbose_name='Страна производитель')
    description = models.TextField(null=True, verbose_name='Описание')
    logo = models.ImageField(verbose_name='Логотип')

    def __str__(self):
        return self.title


class Car(models.Model):
    brand = models.ForeignKey(verbose_name='Марка')
    photo = models.ImageField(verbose_name='Фотография авто')
    model = models.CharField(verbose_name='Модель')
    model_year = models.IntegerField(verbose_name='Год выпуска')

    def __str__(self):
        return '{} {}'.format(self.brand, self.model)


class CarInfo(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')


class CarNote(models.Model):
    note_id = models.ForeignKey(CarInfo, on_delete=models.CASCADE)
    position = models.IntegerField(verbose_name='Позиция текста')
    title = models.CharField(null=True, verbose_name='Описание')
    content = models.TextField(verbose_name='Содержание')


class CarImage(models.Model):
    note_id = models.ForeignKey(CarInfo, on_delete=models.CASCADE)
    position = models.IntegerField(verbose_name='Позиция картинки')
    image = models.ImageField(verbose_name='Картинка')
    description = models.CharField(null=True, verbose_name='Описание')
