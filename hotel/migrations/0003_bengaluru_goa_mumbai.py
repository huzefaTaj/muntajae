# Generated by Django 3.1.1 on 2020-09-25 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_pune'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bengaluru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=50)),
                ('hotel_price', models.IntegerField()),
                ('images', models.ImageField(default='', upload_to='shop/images')),
                ('desc', models.CharField(max_length=300)),
                ('category', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Goa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=50)),
                ('hotel_price', models.IntegerField()),
                ('images', models.ImageField(default='', upload_to='shop/images')),
                ('desc', models.CharField(max_length=300)),
                ('category', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mumbai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=50)),
                ('hotel_price', models.IntegerField()),
                ('images', models.ImageField(default='', upload_to='shop/images')),
                ('desc', models.CharField(max_length=300)),
                ('category', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
