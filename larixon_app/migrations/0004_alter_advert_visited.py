# Generated by Django 4.2.5 on 2023-09-21 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('larixon_app', '0003_alter_advert_visited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='visited',
            field=models.IntegerField(blank=True, default=0, editable=False),
        ),
    ]