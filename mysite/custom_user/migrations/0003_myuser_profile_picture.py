# Generated by Django 3.0.3 on 2020-03-16 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0002_auto_20200316_0329'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='profile_picture',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
