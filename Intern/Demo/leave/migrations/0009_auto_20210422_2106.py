# Generated by Django 3.1.4 on 2021-04-22 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0008_auto_20210422_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hr_login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=5)),
                ('n_pass', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='addman',
            name='n_pass',
            field=models.CharField(max_length=10),
        ),
    ]