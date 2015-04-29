from django.conf.urls import patterns,url

from daodejing import views

urlpatterns=patterns('',
                     url(r'^$',views.index,name='index'),
                     url(r'^(?P<daodej_id>\d+)/$',views.detail,name='detail'),
                     url(r'^getone/$',views.getone,name='getone'),
                     url(r'^(?P<poll_id>\d+)/results/$',views.results,name='results'),
                     url(r'^(?P<poll_id>\d+)/vote/$',views.vote,name='vote'),
                     )
