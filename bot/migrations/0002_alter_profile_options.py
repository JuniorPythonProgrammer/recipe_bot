# Generated by Django 4.1.2 on 2022-10-19 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Користувач', 'verbose_name_plural': 'Користувачі'},
        ),
    ]