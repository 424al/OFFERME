# Generated by Django 3.0.2 on 2020-02-02 00:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0007_auto_20200202_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 2, 0, 15, 10, 604402, tzinfo=utc), verbose_name='date created'),
        ),
    ]
