# Generated by Django 4.2.1 on 2023-06-10 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default=''),
        ),
    ]
