# Generated by Django 5.0.4 on 2024-07-23 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default-profile.png', upload_to='Profile_Images'),
        ),
    ]
