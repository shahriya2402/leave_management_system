# Generated by Django 3.1.4 on 2021-05-02 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0027_delete_man_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Man_login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=25)),
                ('mid', models.CharField(max_length=25)),
                ('man_pass', models.CharField(max_length=10)),
            ],
        ),
    ]
