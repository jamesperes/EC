# Generated by Django 2.0 on 2017-12-29 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecweb', '0006_auto_20171229_1918'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coordinator',
            options={'permissions': (('view_all_classrooms', 'Can view all classrooms'),)},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={},
        ),
    ]
