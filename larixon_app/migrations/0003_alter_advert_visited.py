# Generated by Django 4.2.5 on 2023-09-21 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('larixon_app', '0002_alter_category_options_alter_city_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='visited',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
