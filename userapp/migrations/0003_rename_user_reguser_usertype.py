# Generated by Django 3.2.8 on 2022-01-29 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_auto_20220129_2036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reguser',
            old_name='user',
            new_name='usertype',
        ),
    ]
