# Generated by Django 3.2.16 on 2023-03-09 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20230308_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='photo',
            field=models.ImageField(blank=True, default='default-image.png', null=True, upload_to=''),
        ),
    ]
