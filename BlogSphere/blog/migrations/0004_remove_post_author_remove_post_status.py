# Generated by Django 4.1.13 on 2024-07-19 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_author_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
    ]
