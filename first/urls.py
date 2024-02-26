"""
URL configuration for first project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from first import settings
from .views import home
from .views import login
from . import settings
from .views import cheap
from .views import signup
from .views import sendmail
from .views import verify_otp
from .views import signin
from .views import lvf
urlpatterns = [
    path('send/',sendmail),
    path('',cheap),
    path('loginotp/',login),
    path('home/',home),
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('signin/',signin,name='signin'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    path('db/abc/verification_success',lvf,name='lvf')
]
