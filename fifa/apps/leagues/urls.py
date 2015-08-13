from django.conf.urls import patterns, url

from .views import LeagueList, LeagueDetail

urlpatterns = patterns(
    '',
    url(r'^$', LeagueList.as_view(), name="list"),
    url(r'^(?P<slug>[\w-]+)/$', LeagueDetail.as_view(), name='league'),
)
