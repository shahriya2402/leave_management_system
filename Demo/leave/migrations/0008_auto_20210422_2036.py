# Generated by Django 3.1.4 on 2021-04-22 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0007_auto_20210422_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('eid', models.CharField(max_length=5)),
                ('email', models.CharField(max_length=50)),
                ('fdate', models.CharField(max_length=50)),
                ('cno', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('n_pass', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Addmanager',
        ),
    ]
