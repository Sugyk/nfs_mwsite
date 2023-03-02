# Generated by Django 4.1.4 on 2023-02-15 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0010_carinfo_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carnote',
            name='content',
            field=models.TextField(blank=True, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='carnote',
            name='title',
            field=models.CharField(blank=True, default='', max_length=100, null='', verbose_name='Описание'),
        ),
    ]