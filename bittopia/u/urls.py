from django.conf.urls import patterns, url

from u import views

urlpatterns = patterns('', url(r'^$', views.index, name='index'),
	url(r'^(?P<user_id>\d+)/$', views.detail, name='detail'))