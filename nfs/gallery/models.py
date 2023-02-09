from django.db import models
from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


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
    title = models.CharField(max_length=30, blank=False, null='', default='')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self) -> str:
        return self.title


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


class Profile(models.Model):
    profile = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_image/')
    status = models.CharField(null=True, max_length=90, blank=True)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def profile_create(sender, instance, created, **kwargs):
    if created:
        print('Creating profile')
        Profile.objects.create(email = instance.email, profile=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def profile_save(sender, instance, **kwargs):
    print('Saving profile', sender, instance, kwargs, instance.profile)
    instance.profile.save()
