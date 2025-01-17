# Generated by Django 3.1.1 on 2020-10-27 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(max_length=9000000)),
                ('uname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('day1', models.IntegerField(max_length=200)),
                ('month1', models.IntegerField(max_length=200)),
                ('year1', models.IntegerField(max_length=200)),
                ('day2', models.IntegerField(max_length=200)),
                ('month2', models.IntegerField(max_length=200)),
                ('year2', models.IntegerField(max_length=200)),
                ('cal', models.IntegerField(max_length=9000000)),
            ],
        ),
    ]
