# Generated by Django 4.1.2 on 2022-10-24 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0010_alter_recipe_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
