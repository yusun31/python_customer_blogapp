# Generated by Django 3.1.13 on 2022-02-14 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='published_date',
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
