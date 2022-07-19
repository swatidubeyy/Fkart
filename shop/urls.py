from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('reset/', views.reset, name="reset"),
    path('contact/', views.contact, name="cont"),
    path('search/', views.search, name="search"),
    path('cart/', views.cart, name="cart"),
    path('orderNow/', views.orderNow, name="order"),
    path('myorder/<str:email>', views.order, name="myorder"),
    path('thankyou/', views.thankyou, name="myorder"),
    path('tracknow/', views.track, name="track"),
    path('register/', views.signup, name="signup"),
    path('loginme/', views.signin, name="signin"),
    path('admin/', admin.site.urls),
    path('products/<int:id>', views.product, name="prod"),

]