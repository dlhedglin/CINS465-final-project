# Generated by Django 3.0.3 on 2020-03-05 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='email',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
