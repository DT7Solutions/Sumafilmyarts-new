# Generated by Django 4.2.6 on 2023-11-06 13:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_jobsummary_alter_application_date_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Jobsummary',
        ),
        migrations.AddField(
            model_name='career',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='career',
            name='dead_line',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='career',
            name='experience',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='career',
            name='gender',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='career',
            name='workingtime',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 6, 18, 32, 20, 818101)),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='Created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 6, 18, 32, 20, 818101)),
        ),
        migrations.AlterField(
            model_name='category',
            name='Created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 6, 18, 32, 20, 818101)),
        ),
        migrations.AlterField(
            model_name='collaboration',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 6, 18, 32, 20, 815999)),
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 6, 18, 32, 20, 817102)),
        ),
        migrations.AlterField(
            model_name='ideas',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 6, 18, 32, 20, 817102)),
        ),
        migrations.AlterField(
            model_name='sponsorship',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 6, 18, 32, 20, 817102)),
        ),
    ]