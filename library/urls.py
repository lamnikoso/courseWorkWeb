# -*- coding: utf-8 -*-
"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls.static import static

from library import settings
from library.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^log_in/$', log_in),
    url(r'^log_out/$', log_out),
    url(r'^$', home_page, name='home'),
    url(r'^news/(\d{1,10})/$', news_more),
    url(r'^book/(\d{1,10})/$', book_more),
    url(r'^news/news_like/$', news_like),
    url(r'^catalog/\d', catalog_genre),
    url(r'^register/$', register),
    url(r'^link_book/$', link_book),
    url(r'^like_book/$', like_book),
    url(r'^search/$', search),
    url(r'^search/books/', search_book),
    url(r'^search/users/', search_user),
    url(r'^search/news/', search_news),
    url(r'^live_search/$', live_search),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
