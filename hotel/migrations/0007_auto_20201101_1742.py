# Generated by Django 3.1.1 on 2020-11-01 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_auto_20201027_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='room',
            field=models.CharField(default=0, max_length=500000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
