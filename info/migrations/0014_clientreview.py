# Generated by Django 5.1.3 on 2024-12-26 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0013_renovationinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('review', models.TextField()),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='client_reviews/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
