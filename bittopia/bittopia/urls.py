from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from bittopia import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bittopia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^u/', include('u.urls')),
)
