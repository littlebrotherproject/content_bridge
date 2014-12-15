from django.conf.urls import patterns, url

from videos import views

urlpatterns = patterns('',
    url(r'^from/email', views.email_handle_incoming),
    url(r'^$', views.index, name='index'),

)
