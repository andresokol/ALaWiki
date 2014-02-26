from django.conf.urls import patterns, url

from pages import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^create/$', views.create_article, name='index'),
        url(r'^(?P<title>\w+)/$', views.get_article, name='article'),
        url(r'^(?P<title>\w+)/edit/$', views.edit_article, name='edit'),
        url(r'^(?P<title>\w+)/submit/$', views.submit_changes, name='submit'),
)

