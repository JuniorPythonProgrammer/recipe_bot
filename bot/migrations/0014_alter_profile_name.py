# Generated by Django 4.1.2 on 2022-10-27 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0013_remove_profile_telegram_name_profile_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
