"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from dashboard2 import views
from myanalysis import Myanalysis

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('d1',views.d1, name='d1'),
    path('d2',views.d2, name='d2'),
    path('d3',views.d3, name='d3'),
    path('coin',Myanalysis.coin, name='coin'),

]
