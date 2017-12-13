# Generated by Django 2.0 on 2017-12-11 00:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pdf_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=50)),
                ('file', models.FileField(blank=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=50)),
                ('link', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='pdf',
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='students',
        ),
        migrations.AddField(
            model_name='classroom',
            name='students',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='youtube',
        ),
        migrations.AddField(
            model_name='classroom',
            name='pdf',
            field=models.ManyToManyField(to='ecweb.Pdf_file'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='youtube',
            field=models.ManyToManyField(to='ecweb.Youtube'),
        ),
    ]