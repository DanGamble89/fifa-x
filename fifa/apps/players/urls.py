from django.conf.urls import patterns, url

from .views import PlayerList, PlayerDetail

urlpatterns = patterns(
    '',
    url(r'^$', PlayerList.as_view(), name="player_list"),
    url(r'^(?P<slug>[\w-]+)/$', PlayerDetail.as_view(), name='player_detail'),
)
