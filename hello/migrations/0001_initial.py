# Generated by Django 4.2.2 on 2023-06-08 07:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('path', models.CharField(max_length=100)),
                ('upload_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
