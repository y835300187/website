"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('one/', views.one),
    path('oneone/', views.oneone),
    path('onetwo/', views.onetwo),
    path('onethree/', views.onethree),
    path('onefour/', views.onefour),
    path('onefive/', views.onefive),
    path('onesix/', views.onesix),
    path('oneseven/', views.oneseven),
    path('oneeight/', views.oneeight),
    path('onenine/', views.onenine),
    path('oneten/', views.oneten),
    path('two/', views.two),
    path('twoone/', views.twoone),
    path('twotwo/', views.twotwo),
    path('twothree/', views.twothree),
    path('twofour/', views.twofour),
    path('twofive/', views.twofive),
    path('twosix/', views.twosix),
    path('three/', views.three),
    path('threeone/', views.threeone),
    path('threetwo/', views.threetwo),
    path('threethree/', views.threethree),
    path('threefour/', views.threefour),
]
