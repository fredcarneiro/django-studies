from django.conf.urls import patterns, include, url
from django.contrib import admin
from profiles import views 

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^profiles/(?P<profile_id>\d+)$', views.show, name='show'),
    url(r'^profiles/(?P<profile_id>\d+)/invite$', views.invite, name='invite'),
    url(r'^invitation/(?P<invitation_id>\d+)/aceitar$', views.accept_invitation, name='accept_invitation')
)
