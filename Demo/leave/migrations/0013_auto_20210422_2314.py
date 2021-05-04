# Generated by Django 3.1.4 on 2021-04-22 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0012_auto_20210422_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('mid', models.CharField(max_length=5)),
                ('email', models.CharField(max_length=50)),
                ('fdate', models.CharField(max_length=50)),
                ('cno', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('man_pass', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Addman',
        ),
        migrations.RenameField(
            model_name='addemp',
            old_name='m_pass',
            new_name='e_pass',
        ),
    ]