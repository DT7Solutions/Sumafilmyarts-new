# Generated by Django 4.2.6 on 2023-11-03 09:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_application_date_alter_blogpost_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 14, 54, 37, 435795)),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='Created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 14, 54, 37, 435795)),
        ),
        migrations.AlterField(
            model_name='category',
            name='Created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 14, 54, 37, 435795)),
        ),
        migrations.AlterField(
            model_name='collaboration',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 14, 54, 37, 435795)),
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 14, 54, 37, 435795)),
        ),
        migrations.AlterField(
            model_name='ideas',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 14, 54, 37, 435795)),
        ),
        migrations.AlterField(
            model_name='sponsorship',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 14, 54, 37, 435795)),
        ),
    ]
