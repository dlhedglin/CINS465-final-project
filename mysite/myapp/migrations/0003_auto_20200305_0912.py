# Generated by Django 3.0.3 on 2020-03-05 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_artist_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='artist',
            name='insta_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]