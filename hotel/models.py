from django.db import models

# Create your models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    desc = models.CharField(max_length=1000)
    def __str__(self):
        return self.name

        
class Product(models.Model):
    hotel_id=models.AutoField
    hotel_name=models.CharField(max_length=50)
    hotel_price=models.IntegerField()
    images = models.ImageField(upload_to="shop/images", default="")
    desc=models.CharField(max_length=300)
    category = models.CharField(max_length=50, default="")
    def __str__(self):
        return self.hotel_name

class Pune(models.Model):
    hotel_id=models.AutoField
    hotel_name=models.CharField(max_length=50)
    hotel_price=models.IntegerField()
    images = models.ImageField(upload_to="shop/images", default="")
    desc=models.CharField(max_length=300)
    category = models.CharField(max_length=50, default="")
    def __str__(self):
        return self.hotel_name

class Bengaluru(models.Model):
    hotel_id=models.AutoField
    hotel_name=models.CharField(max_length=50)
    hotel_price=models.IntegerField()
    images = models.ImageField(upload_to="shop/images", default="")
    desc=models.CharField(max_length=300)
    category = models.CharField(max_length=50, default="")
    def __str__(self):
        return self.hotel_name


class Mumbai(models.Model):
    hotel_id=models.AutoField
    hotel_name=models.CharField(max_length=50)
    hotel_price=models.IntegerField()
    images = models.ImageField(upload_to="shop/images", default="")
    desc=models.CharField(max_length=300)
    category = models.CharField(max_length=50, default="")
    def __str__(self):
        return self.hotel_name

class Goa(models.Model):
    hotel_id=models.AutoField
    hotel_name=models.CharField(max_length=50)
    hotel_price=models.IntegerField()
    images = models.ImageField(upload_to="shop/images", default="")
    desc=models.CharField(max_length=300)
    category = models.CharField(max_length=50, default="")
    def __str__(self):
        return self.hotel_name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    username= models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    price= models.CharField(max_length=500000)
    uname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    room= models.CharField(max_length=500000)
    day1=  models.CharField(max_length=500000)
    month1= models.CharField(max_length=500000)
    year1= models.CharField(max_length=500000)
    day2= models.CharField(max_length=500000)
    month2= models.CharField(max_length=500000)
    year2= models.CharField(max_length=500000)
    cal= models.CharField(max_length=500000)
    def __str__(self):
        return self.uname
