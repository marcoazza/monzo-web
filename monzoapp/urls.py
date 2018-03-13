"""monzoapp URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from core import views as core_views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    url(r'^$', core_views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^accounts/login/$', LoginView.as_view(template_name='core/login.html'), name='login'),
    url(r'^transactions/(?P<account_id>\w+)/$', core_views.details, name='transactions'),
    url(r'^logout$', LogoutView.as_view(template_name='core/login.html'), name='logout'),
]
