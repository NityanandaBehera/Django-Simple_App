# Generated by Django 3.2.8 on 2022-01-29 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0005_delete_reguser'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('usertype', models.CharField(choices=[('Doc', 'Doctor'), ('Patients', 'Patients')], max_length=20)),
            ],
        ),
    ]
