# Generated by Django 3.1 on 2023-05-16 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='startDateTime',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Басталу күні мен уақыты'),
        ),
    ]
