# Generated by Django 4.0.7 on 2023-02-08 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0023_comment_title_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='title_link',
        ),
    ]
