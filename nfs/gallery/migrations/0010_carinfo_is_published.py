# Generated by Django 4.1.4 on 2023-02-08 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_carinfo_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='carinfo',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]