# Generated by Django 3.1.1 on 2020-10-27 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cal',
            field=models.CharField(max_length=500000),
        ),
        migrations.AlterField(
            model_name='order',
            name='day1',
            field=models.CharField(max_length=500000),
        ),
        migrations.AlterField(
            model_name='order',
            name='day2',
            field=models.CharField(max_length=500000),
        ),
        migrations.AlterField(
            model_name='order',
            name='month1',
            field=models.CharField(max_length=500000),
        ),
        migrations.AlterField(
            model_name='order',
            name='month2',
            field=models.CharField(max_length=500000),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.CharField(max_length=500000),
        ),
        migrations.AlterField(
            model_name='order',
            name='year1',
            field=models.CharField(max_length=500000),
        ),
        migrations.AlterField(
            model_name='order',
            name='year2',
            field=models.CharField(max_length=500000),
        ),
    ]
