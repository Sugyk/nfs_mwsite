# Generated by Django 4.1.4 on 2023-02-15 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0015_carnote_description_carnote_image_delete_carimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carnote',
            name='image',
            field=models.ImageField(blank=True, default='plug.jpg', upload_to='', verbose_name='Картинка'),
        ),
    ]
