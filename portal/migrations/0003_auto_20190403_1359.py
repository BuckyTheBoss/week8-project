# Generated by Django 2.1.7 on 2019-04-03 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20190403_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
