from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from forums import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('forums.views',
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^topics/$', views.TopicList.as_view()),
    url(r'^topics/(?P<pk>[0-9]+)/$', views.TopicDetail.as_view()),
    url(r'^comments/$', views.CommentList.as_view()),
    url(r'^comments/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view()),
    url(r'^reply/$', views.ReplyList.as_view()),
    url(r'^reply/(?P<pk>[0-9]+)/$', views.ReplyDetail.as_view()),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns = format_suffix_patterns(urlpatterns)