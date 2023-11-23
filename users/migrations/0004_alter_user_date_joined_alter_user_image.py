# Generated by Django 4.2.7 on 2023-11-23 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='users/images/default.img', upload_to='users/images'),
        ),
    ]