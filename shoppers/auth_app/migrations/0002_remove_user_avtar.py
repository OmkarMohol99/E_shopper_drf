# Generated by Django 4.1.1 on 2022-09-26 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avtar',
        ),
    ]
