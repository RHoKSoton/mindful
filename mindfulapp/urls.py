from django.conf.urls import patterns, include, url
from mindfulapp import views

urlpatterns = patterns('',
	url(r'^$', views.landing, name="landing"),
  url(r'^user/(?P<id>\d+)$',views.user,name="user"),
	url(r'^user/(?P<id>\d+)/play$', views.user_play, name="user_play"),
	url(r'^carer/(?P<id>\d+)$', views.carer, name="carer"),
	url(r'^carer/(?P<carer_id>\d+)/user/(?P<user_id>\d+)$', views.view_user, name="view_user"),
	url(r'^observation/(?P<carerid>\d+)/(?P<listenid>\d+)$', views.observation, name="observation"),
	url(r'^$', views.index, name='index'),
	url(r'^login$', views.login_user, name="login_user"),
	url(r'^login-carer$', views.login_carer, name="login_carer"),
	url(r'^logout$', views.logout, name="logout")
)
