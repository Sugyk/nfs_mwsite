# Generated by Django 4.1.4 on 2023-02-08 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='carinfo',
            name='title',
            field=models.CharField(default='', max_length=30, null=''),
        ),
    ]
