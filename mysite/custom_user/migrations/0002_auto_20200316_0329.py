# Generated by Django 3.0.3 on 2020-03-16 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='instagram_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
