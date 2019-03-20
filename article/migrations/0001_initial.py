# Generated by Django 2.1.7 on 2019-03-20 11:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=datetime.datetime(2019, 3, 20, 11, 38, 5, 757883, tzinfo=utc))),
            ],
        ),
    ]