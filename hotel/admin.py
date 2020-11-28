from django.contrib import admin
from .models import Contact,Order,Product,Pune,Bengaluru,Mumbai,Goa
# Register your models here.
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Pune)
admin.site.register(Bengaluru)
admin.site.register(Mumbai)
admin.site.register(Goa)