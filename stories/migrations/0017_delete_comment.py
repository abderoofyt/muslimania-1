# Generated by Django 4.0.7 on 2023-02-07 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0016_delete_comments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
