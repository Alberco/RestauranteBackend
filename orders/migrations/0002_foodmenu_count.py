# Generated by Django 4.1.2 on 2022-10-14 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodmenu',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
