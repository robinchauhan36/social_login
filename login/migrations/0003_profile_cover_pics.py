# Generated by Django 3.0.3 on 2020-02-19 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20200219_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cover_pics',
            field=models.ImageField(default='default.jpg', upload_to='cover_pics'),
        ),
    ]
