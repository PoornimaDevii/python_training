"""mysite URL Configuration

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
from django.urls import include,path,re_path
from myapp.views import *
# for path name ^hello/$ matches exactly, hello/$ matches hello at the end,
# need to give url as 127.0.0.1:8000/hello/poornima/

urlpatterns = [
    re_path('hello/(\w+)',say_hello),
    path('time/',current_datetime),
    re_path('hours/(\d+)',hours_ahead),
    path('admin/', admin.site.urls),
    path('test/',current_datetime1),
    path('form/',create_form),
    path('search/',search),
    #path('form1/',render_made_form),
    path('get_color/',get_color),
    path('set_color/',set_color),
    path('show_color1/',show_color),
    path('loginp/',login_page),
    path('loginn/',login_as_user),
    path('loginn1/',return_to_search)
]
