"""
URL configuration for ownCity project.

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
from django.urls import re_path
from django.views.generic import TemplateView

urlpatterns = [
    re_path(r'^news', TemplateView.as_view(template_name="news.html")),
    re_path(r'^goverment', TemplateView.as_view(template_name="goverment.html")),
    re_path(r'^facts', TemplateView.as_view(template_name="facts.html")),
    re_path(r'^contacts', TemplateView.as_view(template_name="contacts.html")),
    re_path(r'^history/people', TemplateView.as_view(template_name="people.html")),
    re_path(r'^history/photos', TemplateView.as_view(template_name="photos.html")),
    re_path(r'^history', TemplateView.as_view(template_name="history.html")),
    re_path(r'^$', TemplateView.as_view(template_name="index.html")),
    path('admin/', admin.site.urls),
]
