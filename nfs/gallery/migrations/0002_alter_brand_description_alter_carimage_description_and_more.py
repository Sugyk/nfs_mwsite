# Generated by Django 4.1.4 on 2022-12-30 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='carimage',
            name='description',
            field=models.CharField(blank=True, max_length=70, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='carnote',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Описание'),
        ),
    ]