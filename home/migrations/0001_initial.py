# Generated by Django 3.0.4 on 2020-10-24 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addemp',
            fields=[
                ('yourid', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('male', models.CharField(max_length=100)),
                ('female', models.CharField(max_length=100)),
                ('other', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
                ('pancard', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
            ],
        ),
    ]