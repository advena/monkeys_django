from django.conf.urls import patterns, url
from monkeys import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	)