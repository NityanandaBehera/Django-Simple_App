# Generated by Django 3.2.8 on 2022-01-29 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_rename_user_reguser_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reguser',
            name='password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='reguser',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
