# Generated by Django 4.1.6 on 2023-02-15 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_review_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(to='projects.tag'),
        ),
    ]