# Generated by Django 4.2.6 on 2023-11-03 09:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_blogposts_alter_application_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(default='title', max_length=225)),
                ('Description', models.CharField(blank=True, max_length=2000, null=True)),
                ('Image1', models.ImageField(upload_to='uploads/')),
                ('Body', models.TextField(blank=True, null=True)),
                ('Sluglink', models.CharField(blank=True, max_length=200, null=True)),
                ('CreatedName', models.CharField(max_length=100)),
                ('Created_at', models.DateTimeField(default=datetime.datetime(2023, 11, 3, 14, 48, 33, 724402))),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='heading', max_length=30)),
                ('Created', models.DateTimeField(default=datetime.datetime(2023, 11, 3, 14, 48, 33, 724402))),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.DeleteModel(
            name='Blogposts',
        ),
        migrations.AlterField(
            model_name='application',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 14, 48, 33, 724402)),
        ),
        migrations.AlterField(
            model_name='collaboration',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 14, 48, 33, 724402)),
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 14, 48, 33, 724402)),
        ),
        migrations.AlterField(
            model_name='ideas',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 14, 48, 33, 724402)),
        ),
        migrations.AlterField(
            model_name='sponsorship',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 14, 48, 33, 724402)),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Categories', to='app.category'),
        ),
    ]
