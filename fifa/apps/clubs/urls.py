from django.conf.urls import patterns, url

from .views import ClubList, ClubDetail

urlpatterns = patterns(
    '',
    url(r'^$', ClubList.as_view(), name="list"),
    url(r'^(?P<slug>[\w-]+)/$', ClubDetail.as_view(), name='club'),
)
