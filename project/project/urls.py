"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from recipe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('detail/<int:recipe_pk>/',views.detail, name='detail'),
    path('total_list', views.total_list, name='total_list'),
    path('keyword', views.keyword, name='keyword'),
    path('goso', views.goso, name='goso'),
    path('sweet', views.sweet, name='sweet'),
    path('spicy', views.spicy, name='spicy'),
    path('sour', views.sour, name='sour'),
    path('salty', views.salty, name='salty'),

]
