# Generated by Django 4.1.4 on 2023-01-25 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_movie_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
    ]
