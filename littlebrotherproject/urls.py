from django.conf.urls import patterns, include, url
from django.contrib import admin
from videos import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'littlebrotherproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^video/', include('videos.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
