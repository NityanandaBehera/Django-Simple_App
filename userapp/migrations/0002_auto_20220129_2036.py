# Generated by Django 3.2.8 on 2022-01-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reguser',
            name='password',
            field=models.CharField(default='defpass', max_length=20),
        ),
        migrations.AddField(
            model_name='reguser',
            name='username',
            field=models.CharField(default='def', max_length=20),
        ),
    ]
