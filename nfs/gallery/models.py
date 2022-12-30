from django.db import models


class Brand(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название бренда')
    country = models.CharField(max_length=50, verbose_name='Страна производитель')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    logo = models.ImageField(upload_to='media/', verbose_name='Логотип')

    def __str__(self):
        return self.title


class Car(models.Model):
    brand = models.ForeignKey(Brand,on_delete=models.PROTECT, verbose_name='Марка')
    photo = models.ImageField(upload_to='media/', verbose_name='Фотография авто')
    short_description = models.CharField(max_length=100, verbose_name='Краткое описание', default='Описание отсутсвует')
    model = models.CharField(max_length=50, verbose_name='Модель')
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
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='Описание')
    content = models.TextField(verbose_name='Содержание')


class CarImage(models.Model):
    note_id = models.ForeignKey(CarInfo, on_delete=models.CASCADE)
    position = models.IntegerField(verbose_name='Позиция картинки')
    image = models.ImageField(verbose_name='Картинка')
    description = models.CharField(null=True, max_length=70, blank=True, verbose_name='Описание')
