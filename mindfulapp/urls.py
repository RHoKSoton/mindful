from django.conf.urls import patterns, include, url
from mindfulapp import views

urlpatterns = patterns('',
	url(r'^user/(?P<id>\d+)$', views.user, name="user"),
	url(r'^$', views.index, name='index'),
	url(r'^login$', views.login_user, name="login_user"),
	url(r'^login-carer$', views.login_carer, name="login_carer"),
	url(r'^logout$', views.logout, name="logout")
)
