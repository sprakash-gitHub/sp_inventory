# Generated by Django 5.0.4 on 2024-06-09 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default-profile.png', upload_to='Profile_Images'),
        ),
    ]
