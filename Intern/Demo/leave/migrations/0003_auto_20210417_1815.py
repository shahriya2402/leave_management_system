# Generated by Django 3.1.4 on 2021-04-17 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0002_rename_contact_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]