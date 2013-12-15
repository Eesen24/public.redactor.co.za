from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from forums import views

urlpatterns = patterns('forums.views',
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^topics/$', views.TopicList.as_view()),
    url(r'^topics/(?P<pk>[0-9]+)/$', views.TopicDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)