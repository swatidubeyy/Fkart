from django.shortcuts import render
from  django.http import HttpResponse
from .models import Products,Contact,Order,TrackOrder,Users
from math import ceil
import random
# Create your views here.
def index(request):
         login='true'
         aprod=[]
         catprod=Products.objects.values('categoty','id')
         cats={item['categoty'] for item in catprod}
         for cat in cats:
            prod= Products.objects.filter(categoty=cat)
            n = len(prod)
            nos = n // 4 + ceil((n / 4) - (n // 4))
            aprod.append([prod,range(1,nos),nos])
         params={'allprod':aprod}
         return render(request,"shop/index.html",params)

def searchMatch(query,item):
   if query in item.product_Name.lower() or query in item.categoty.lower() or query in item.product_Description.lower():
      return True
   else:
      return False

def search(request):
   query=request.GET.get("search")
   aprod = []
   catprod = Products.objects.values('categoty', 'id')
   cats = {item['categoty'] for item in catprod}
   for cat in cats:
      prodtemp = Products.objects.filter(categoty=cat)
      prod=[i for i in prodtemp if searchMatch(query,i)]
      n = len(prod)
      nos = n // 4 + ceil((n / 4) - (n // 4))
      if len(prod) != 0:
       aprod.append([prod, range(1, nos), nos])
   params = {'allprod': aprod,"msg":""}
   if len(aprod)==0 or len(query)<4:
         params={"msg":"Sorry, No item,we can add item in future"}
   return render(request, "shop/index.html", params)
def about(request):
   return render(request,"shop/about.html",)
def product(request,id):
   myid=id
   products=Products.objects.filter(id=myid)
   return render(request,"shop/product.html",{'product':products[0]})
def contact(request):
   if request.method=="POST":
      name=request.POST.get('name')
      email = request.POST.get('email')
      mobile = request.POST.get('mob')
      a=int(len(mobile))
      if a<10 or a>10:
         print(len(mobile))
         return render(request, "shop/contact.html",{"error":"Invalid mobile Number"} )

      msg = request.POST.get('con')
      con=Contact(Name=name,Email=email,Mobile=mobile,Message=msg)
      con.save()
      return render(request, "shop/contact.html", {'error': 'Succesfully send'})
   else:
     return render(request,"shop/contact.html",{'error':'none'})
def cart(request):
   return render(request,"shop/cart.html",{'msg':'none'})
thanks=1
def orderNow(request):
   global thanks;
   thanks+=1
   if request.method == 'POST':
      name=request.POST.get('name')
      email = request.POST.get('email')
      mobile = request.POST.get('mobile')
      almobile = request.POST.get('almobile')
      address = request.POST.get('address')
      land= request.POST.get('address2')
      city = request.POST.get('city')
      state = request.POST.get('state')
      zip = request.POST.get('zipcode')
      items=request.POST.get('items')
      price = request.POST.get('price')
      if items!=''  and  thanks%2==0:
         order=Order(Name=name,Email=email,Mobile=mobile,Alternative_Mobile=almobile,Address=address,landmark=land,City=city,State=state,Zip=zip,Orders=items,price=price)
         order.save()
         id=order.orderid
         number=random.randint(1000,100000)
         idnew='IKART'+str(number)+str(id)
         saveid=Order.objects.get(pk=id)
         saveid.Track_Id=idnew
         saveid.save()
         trackorder=TrackOrder(Order_id=idnew,Email=email,order_Description='Your Order Has Been Placed')
         trackorder.save()
         return render(request, "shop/thankyou.html",{'id':idnew} )

      if items!='' and thanks % 2 != 0:
         return render(request, "shop/cart.html", {'msg':'none'})
      else:
         msg = 'Your Cart Is Empty! Please Add Some Items In Your Cart First...'
         return render(request, "shop/cart.html", {'msg': msg})
def order(request,email):
   email=email.replace('"','')
   emails=email
   products=Order.objects.filter(Email=emails)
   print(len(products))
   a=[]
   if len(products)<0:
     msg='none'
   else:
      msg='true'
      for items in products:
           a.append([items.Orders, items.price, items.Track_Id])
   print(a)
   print(msg)
   return render(request, "shop/order.html",{'product':a,'msg':msg})

def thankyou(request):
   if request.method=='POST':
      return render(request, "shop/thankyou.html")
   else:
       return render(request, "shop/cart.html",{'msg':'none'})
def track(request):
   if request.method == "POST":
            email=request.POST.get('email')
            tid = request.POST.get('tid')
            print(len(email))
            info = TrackOrder.objects.filter(Email=email, Order_id=tid)
            print(info)
            if len(info)>0:
               a=[]
               for items in info:
                  a.append([items.order_Description,str(items.Date)[0:24],str(items.Time)[0:8]])
               return render(request, "shop/track.html",{'result':a,'msg':'none'})
            else:
               return render(request, "shop/track.html", {'result': 'none', 'msg': 'No Item Found For This TrackId'})

   else:
      return render(request, "shop/track.html", {'result':'none', 'msg': 'none'})


def signup(request):
   if request.method == 'POST':
      name = request.POST.get('name')
      email = request.POST.get('email')
      mobile = request.POST.get('mob')
      password = request.POST.get('pass')
      cpass=request.POST.get('cpass')
      check_email=Users.objects.filter(Email=email)
      if len(check_email)>0:
        return render(request, 'front.html', {'msg': 'Email already exist!'})
      elif cpass!=password:
         return render(request, 'front.html', {'msg': 'Password And Confirm Password Does Not Match'})
      user = Users(Password=password, Name=name, Email=email, Mobile=mobile)
      user.save()
      return render(request, 'front.html',{'msg':'Account Created SUccessfully! Please login To Enter shop'})
   else:
      return render(request, 'front.html',{'msg':'none'})
def signin(request):
   if request.method == 'POST':
      password = request.POST.get('passlogin')
      email = request.POST.get('emaillogin')
      check=Users.objects.filter(Email=email,Password=password)
      if len(check)>0:
         return render(request, 'shop/index.html',{'msg':'none'})
      else:
         return render(request, 'front.html', {'msg': 'Your Password does not matched,Please Try Again'})
   else:
      return render(request, 'front.html',{'msg':'none'})


def reset(request):
   if request.method == 'POST':
     name=request.POST.get("reemail")
     mobile=request.POST.get("remobile")
     pas=request.POST.get("resetpass")
     user=Users.objects.filter(Email=name,Mobile=mobile)
     if len(user) > 0:
        usey = Users(Password=pas, Email=name, Mobile=mobile)
        usey.save()
        return render(request, 'front.html', {'msg': 'reset password successfull'})
     else:
      return render(request, 'front.html', {'msg': 'Your mobile and email does not matched,Please Try Again'})
   else:
     return render(request, 'front.html', {'msg': 'none'})