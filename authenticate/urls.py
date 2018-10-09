from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^register/$', views.register_user, name='register'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^change_password/$', views.change_password, name='change_password'),



]
