# Generated by Django 5.1.3 on 2024-12-25 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='button_link',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='button_text',
        ),
    ]
