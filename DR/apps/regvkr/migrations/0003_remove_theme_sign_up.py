# Generated by Django 3.0.4 on 2020-03-09 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regvkr', '0002_auto_20200306_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='sign_up',
        ),
    ]