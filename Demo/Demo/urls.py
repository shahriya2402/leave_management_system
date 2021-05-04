"""Demo URL Configuration

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
from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('e_login', views.e_login, name='e_login'),
    path('m_login', views.m_login, name='m_login'),
    path('hr_login', views.hr_login, name='hr_login'),
    path('registration', views.registration, name='registration'),
    path('hr', views.hr, name='hr'),
    path('addmanager', views.addmanager, name='addmanager'),
    path('addemployee', views.addemployee, name='addemployee'),
    path('gallery', views.gallery, name='gallery'),
    path('reg', views.reg, name='reg'),
    path('manager', views.manager, name='manager'),
    path('employee', views.employee, name='employee'),
    path('eleave', views.eleave, name='eleave'),
    path('viewleave', views.viewleave, name='viewleave'),
    path('firstindex', views.firstindex, name='firstindex'),
    path('myleave', views.myleave, name='myleave'),
    path('status', views.status, name='status'),
    path('status1', views.status1, name='status1'),
    path('myleave1', views.myleave1, name='myleave1'),
    path('viewleave1', views.viewleave1, name='viewleave1'),
    path('mleave', views.mleave, name='mleave'),

    path('index/e_login', views.e_login, name='e_login'),
    path('index/m_login', views.m_login, name='m_login'),
    path('index/hr_login', views.hr_login, name='hr_login'),
    path('index/hr', views.hr, name='hr'),
    path('addmanager/addmanager', views.addmanager, name='addmanager'),
    path('addmanager/hr_login', views.hr_login, name='hr_login'),
    path('hr_login/hr', views.hr, name='hr'),
    path('hr_login/addmanager', views.addmanager, name='addmanager'),
    path('hr/viewleave1', views.viewleave1, name='viewleave1'),
    path('manager/manager',views.manager, name='manager'),
    path('m_login/manager', views.manager, name='manager'),
    path('manager/m_login',views.m_login, name='m_login'),
    path('employee/myleave', views.myleave, name='myleave'),
    path('manager/myleave1', views.myleave1, name='myleave1'),
    path('m_login/myleave1', views.myleave1, name='myleave1'),
    path('eleave/myleave', views.myleave, name='myleave'),
    path('m_login/viewleave', views.viewleave, name='viewleave'),
    path('viewleave/accept', views.accept, name='accept'),
    path('viewleave1/accept1', views.accept1, name='accept1'),
    path('m_login/accept', views.accept, name='accept'),
    path('hr_login/accept1', views.accept1, name='accept1'),
    path('hr_login/reject1', views.reject1, name='reject1'),
    path('m_login/reject', views.reject, name='reject'),
    path('m_login/eleave', views.eleave, name='eleave'),
    path('m_login/addemployee', views.addemployee, name='addemployee'),
    path('e_login/myleave', views.myleave, name='myleave'),
    path('m_login/mleave', views.mleave, name='mleave'),
    path('m_login/aleave', views.aleave, name='aleave'),
    path('hr_login/aleave1', views.aleave1, name='aleave1'),
    path('m_login/rleave', views.rleave, name='rleave'),
    path('hr_login/rleave1', views.rleave1, name='rleave1'),
    path('hr_login/viewleave1', views.viewleave1, name='viewleave1'),
    path('m_login/m_login', views.m_login, name='m_login'),
    path('hr_login/hr_login', views.hr_login, name='hr_login'),


]
