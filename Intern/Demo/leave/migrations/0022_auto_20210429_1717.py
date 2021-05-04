# Generated by Django 3.1.4 on 2021-04-29 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0021_auto_20210425_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=5)),
                ('sdate', models.CharField(max_length=15)),
                ('edate', models.CharField(max_length=15)),
                ('ltype', models.CharField(max_length=50)),
                ('rsn', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='eleave',
            name='is_approved',
        ),
    ]
