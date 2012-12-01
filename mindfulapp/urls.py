from django.conf.urls import patterns, include, url
from mindfulapp import views

urlpatterns = patterns('',
	url(r'^patient/(?P<id>\d+)$', views.patient, name="patient"),
	url(r'^$', views.index, name='index'),
	url(r'^login$', views.login_patient, name="login_patient"),
	url(r'^login-carer$', views.login_carer, name="login_carer"),
	url(r'^logout$', views.logout, name="logout")
)
