# Generated by Django 2.1.2 on 2018-11-21 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('slug', models.SlugField(blank=True, default='')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
