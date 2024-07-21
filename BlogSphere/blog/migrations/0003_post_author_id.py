# Generated by Django 4.1.13 on 2024-07-19 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_user_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='blog.user'),
            preserve_default=False,
        ),
    ]
