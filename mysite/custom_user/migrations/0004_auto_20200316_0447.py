# Generated by Django 3.0.3 on 2020-03-16 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0003_myuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profile_picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
