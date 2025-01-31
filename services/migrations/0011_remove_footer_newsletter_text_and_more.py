# Generated by Django 5.1.3 on 2025-01-11 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_footer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footer',
            name='newsletter_text',
        ),
        migrations.RemoveField(
            model_name='footer',
            name='newsletter_text_az',
        ),
        migrations.RemoveField(
            model_name='footer',
            name='newsletter_text_en',
        ),
        migrations.RemoveField(
            model_name='footer',
            name='newsletter_text_ru',
        ),
        migrations.AddField(
            model_name='footer',
            name='facebook_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='instagram_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='whatsapp_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
