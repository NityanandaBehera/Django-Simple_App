# Generated by Django 3.2.8 on 2022-01-30 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_alter_reguserdet_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reguserdet',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='reguserdet',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
