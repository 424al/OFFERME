# Generated by Django 3.0.2 on 2020-02-01 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0004_auto_20200201_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
