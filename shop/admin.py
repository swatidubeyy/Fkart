from django.contrib import admin
from .models import Products,Contact,Order,TrackOrder,Users
# Register your models here.
admin.site.register(Products)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(TrackOrder)
admin.site.register(Users)
