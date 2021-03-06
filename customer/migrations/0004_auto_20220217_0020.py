# Generated by Django 3.1.13 on 2022-02-16 15:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2022, 2, 16, 15, 20, 6, 821928, tzinfo=utc)),
        ),
    ]
