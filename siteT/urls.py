from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.base),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^signup/user/$', views.signup_user, name='signup_user'),
    url(r'^newevento/evento/$', views.new_evento, name='new_evento'),   
]
