# Generated by Django 3.1.4 on 2021-05-02 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0034_mleave'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acceptreject1',
            old_name='status',
            new_name='status1',
        ),
        migrations.RenameField(
            model_name='viewleave1',
            old_name='status',
            new_name='status1',
        ),
    ]
