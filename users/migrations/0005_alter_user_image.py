# Generated by Django 4.2.7 on 2023-11-23 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_date_joined_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='users/images/default.jpg', upload_to='users/images'),
        ),
    ]
