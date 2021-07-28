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
    path('loading', views.loading, name='index'),
    path('index2', views.index2, name='index2'),
    # path('loading2', views.loading2, name='loading2'),
    path('loading3', views.loading3, name='loading3'),
    path('coin', Myanalysis.Project.coin, name='coin'),
]

