# Generated by Django 4.1.4 on 2023-02-15 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0012_alter_carnote_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carimage',
            name='image',
            field=models.ImageField(blank=True, default='plug.jpg', null='', upload_to='', verbose_name='Картинка'),
        ),
    ]
