# Generated by Django 4.1.2 on 2022-10-28 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0015_alter_profile_last_name_alter_profile_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('чоловік', 'Чоловік'), ('жінка', 'Жінка')], default='чоловік', max_length=7),
        ),
    ]
