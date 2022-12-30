# Generated by Django 4.1.4 on 2022-12-30 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название бренда')),
                ('country', models.CharField(max_length=50, verbose_name='Страна производитель')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('logo', models.ImageField(upload_to='', verbose_name='Логотип')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фотография авто')),
                ('model', models.CharField(max_length=50, verbose_name='Модель')),
                ('model_year', models.IntegerField(verbose_name='Год выпуска')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gallery.brand', verbose_name='Марка')),
            ],
        ),
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.car')),
            ],
        ),
        migrations.CreateModel(
            name='CarNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(verbose_name='Позиция текста')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Описание')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('note_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.carinfo')),
            ],
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(verbose_name='Позиция картинки')),
                ('image', models.ImageField(upload_to='', verbose_name='Картинка')),
                ('description', models.CharField(max_length=70, null=True, verbose_name='Описание')),
                ('note_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.carinfo')),
            ],
        ),
    ]
