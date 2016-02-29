from django.conf.urls import patterns, include, url
"""mysite URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from mysite import views
from django.views.static import serve
from django.views.defaults import bad_request
from django.views.defaults import server_error
from django.views.defaults import page_not_found
from django.views.defaults import permission_denied
from django.views.generic.base import RedirectView
from django.contrib.sitemaps.views import index
from django.contrib.sitemaps.views import sitemap

from django_xmlrpc.views import handle_xmlrpc

from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/about/', permanent=True)),
    url(r'^blog/', include('zinnia.urls', namespace='zinnia')),
	url(r'^blog/', include('zinnia.urls.entries')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^xmlrpc/$', handle_xmlrpc),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', include('zinnia.urls.entries')),
	url(r'^about/$', views.about),
	url(r'^about/blog', views.about),
]

sitemaps = {
    'tags': TagSitemap,
    'blog': EntrySitemap,
    'authors': AuthorSitemap,
    'categories': CategorySitemap
}

urlpatterns += [
    url(r'^sitemap.xml$',
        index,
        {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$',
        sitemap,
        {'sitemaps': sitemaps}),
]

urlpatterns += [
    url(r'^400/$', bad_request),
    url(r'^403/$', permission_denied),
    url(r'^404/$', page_not_found),
    url(r'^500/$', server_error),
]

