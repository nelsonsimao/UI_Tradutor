'''
Created on Dec 23, 2013

@author: nelson
'''
from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
    url(r'^$', views.trad, name='index'),
    url(r'^treino/$', views.treino, name='treino'),
    #url(r'^$', views.index, name='index'),
    #url(r'^trad/$', views.trad, name='trad'),
    #url(r'^result/$', views.result, name='result'),
)