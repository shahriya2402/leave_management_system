# Generated by Django 3.1.4 on 2021-04-22 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0006_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addmanager',
            old_name='job',
            new_name='dept',
        ),
    ]