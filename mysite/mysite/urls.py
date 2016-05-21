"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

import myapp.views

urlpatterns = [
	url(r'^$', myapp.views.index, name='index'),
	url(r'^McGill', myapp.views.mcgill, name='mcgill'),
	url(r'^PacificAcademy', myapp.views.pacificacademy, name='pacificacademy'),
	url(r'^Projects', myapp.views.projects, name='projects'),
	url(r'^Programming/DataStructure', myapp.views.datastructure, name='datastructure'),
	url(r'^Programming/DesignPattern', myapp.views.designpattern, name='designpattern'),
    url(r'^admin/', admin.site.urls),
]
