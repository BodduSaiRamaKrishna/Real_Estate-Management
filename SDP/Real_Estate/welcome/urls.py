"""Real_Estate URL Configuration

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
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.welcome,name='welcome'),
    path('login/',views.loginpage,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logoutUser,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('feedback/',views.feedback,name='feedback'),
    path('help/',views.help,name='help'),
    path('homepage/',views.homepage,name='homepage'),
    path('transaction/',views.transaction,name='transaction'),
    path('land/',views.land,name='land'),
    path('commercial/',views.commercial,name='commercial'),
    path('development/',views.development,name='development'),
    path('industrial/',views.industrial,name='industrial'),
    path('property_management/',views.property_management,name='property_management'),
    path('villa/',views.villa,name='villa'),
    path('details/',views.details,name='details'),
    path('new/',views.new,name='new'),
    path('new1/',views.new1,name='new1'),
    path('property/',views.index,name="property"),
    path('new2/',views.new2,name="new2"),
    path('admin/', admin.site.urls),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
         name="password_reset_complete"),
]
