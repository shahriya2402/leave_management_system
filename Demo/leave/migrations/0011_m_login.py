# Generated by Django 3.1.4 on 2021-04-22 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0010_auto_20210422_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='M_login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.CharField(max_length=5)),
                ('m_pass', models.CharField(max_length=10)),
            ],
        ),
    ]