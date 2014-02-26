from django.conf.urls import patterns, include, url
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

def redirector(request, title):
    return HttpResponseRedirect('/wiki/' + title)

def main_redirector(request):
    return HttpResponseRedirect('/wiki/')


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wiki.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^wiki/', include('pages.urls', namespace="pages")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<title>\w+)/$', redirector, name='redirector'),
    url(r'^$', main_redirector, name='redirector2')
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
