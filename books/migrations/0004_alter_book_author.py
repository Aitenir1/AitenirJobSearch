# Generated by Django 3.2.16 on 2023-03-08 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default='No Author', on_delete=django.db.models.deletion.CASCADE, to='books.author'),
        ),
    ]
