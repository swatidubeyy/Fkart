from django.db import models

# Create your models here.
class Products(models.Model):
    product_Id=models.AutoField
    product_Name=models.CharField(max_length=120)
    product_Description=models.CharField(max_length=30000)
    categoty=models.CharField(max_length=20,default="")
    sub_categoty = models.CharField(max_length=20, default="")
    price=models.IntegerField(default="0")
    product_image=models.ImageField(upload_to="shop/images",default="")
    product_Date=models.DateField()
    def __str__(self):
         return  self.product_Name
class Contact(models.Model):
    msgid=models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50 ,default="")
    Email = models.CharField(max_length=70,default="")
    Mobile = models.IntegerField(default="0")
    Message= models.CharField(max_length=7000,default="")
    def __str__(self):
         return  self.Name
class Order(models.Model):
    orderid=models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50 ,default="")
    Email = models.CharField(max_length=70,default="")
    Mobile = models.IntegerField(default="0")
    Alternative_Mobile = models.IntegerField(default="0")
    Address= models.CharField(max_length=7000,default="")
    landmark = models.CharField(max_length=150, default="")
    City=models.CharField(max_length=50, default="")
    State=models.CharField(max_length=30, default="")
    Zip=models.CharField(max_length=10, default="")
    Orders = models.CharField(max_length=1000000000,default="")
    price = models.IntegerField( default=0)
    Track_Id = models.CharField(max_length=70, default="")
    def __str__(self):
         return  self.Name
class TrackOrder(models.Model):
    orderid=models.AutoField(primary_key=True)
    Order_id = models.CharField(max_length=50, default="")
    Email = models.CharField(max_length=70, default="")
    order_Description=models.CharField(max_length=150, default="")
    Date=models.DateField(auto_now=True, blank=True)
    Time = models.TimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.Order_id
class Users(models.Model):
    orderid = models.AutoField(primary_key=True)
    orderid=models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50 ,default="")
    Email = models.CharField(max_length=70,default="")
    Mobile = models.IntegerField(default="0")
    Password=models.CharField(max_length=70,default="")

    def __str__(self):
         return  self.Name