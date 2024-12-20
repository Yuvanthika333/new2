"""
URL configuration for project1 project.

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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('edit/editrecord/<int:id>',views.editrecord,name='editrecord'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('search/<int:id>',views.delete,name='search'),
    path('contactus/',views.contactus,name='contactus'),
    path('studentlogin/',views.studentlogin,name='studentlogin'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('registor/',views.registor,name='registor'),
    path('admin_reg/',views.admin_reg,name='admin_reg'),
     path('adview/',views.adview,name='adview'),
    path('stud_dash/',views.stud_dash,name='stud_dash',)
]
