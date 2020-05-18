# Generated by Django 3.0.4 on 2020-05-18 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regvkr', '0015_auto_20200518_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='scientificdirector',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='scientificdirector',
            name='is_director',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='student',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='scientificdirector',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='Логин:'),
        ),
        migrations.AlterField(
            model_name='scientificdirector',
            name='first_name',
            field=models.CharField(max_length=15, verbose_name='Имя:'),
        ),
        migrations.AlterField(
            model_name='scientificdirector',
            name='last_name',
            field=models.CharField(max_length=25, verbose_name='Фамилия:'),
        ),
        migrations.AlterField(
            model_name='scientificdirector',
            name='password',
            field=models.CharField(max_length=32, verbose_name='Пароль:'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=15, verbose_name='Имя:'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=25, verbose_name='Фамилия:'),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=32, verbose_name='Пароль:'),
        ),
    ]