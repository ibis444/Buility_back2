# Generated by Django 5.1.3 on 2024-12-25 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_corefeature_corefeaturevideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoreFeatureSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
            ],
        ),
    ]
