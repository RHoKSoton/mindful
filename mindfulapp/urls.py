from django.conf.urls import patterns, include, url

from mindfulapp import views

urlpatterns = patterns('',
	url(r'^patient/(?P<id>\d+)$', views.patient, name="patient"),
	url(r'^$', views.index, name='index')
)
