# Generated by Django 3.1.4 on 2021-05-02 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0035_auto_20210502_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eleave',
            name='rsn',
        ),
    ]
