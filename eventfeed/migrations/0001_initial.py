# Generated by Django 4.1.2 on 2022-10-08 07:39

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=255, populate_from='title', unique=True, verbose_name='url')),
                ('description', models.TextField(max_length=2000)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('image', models.ImageField(default='default.png', upload_to='')),
            ],
        ),
    ]