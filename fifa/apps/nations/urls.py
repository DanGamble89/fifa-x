from django.conf.urls import patterns, url

from .views import NationList, NationDetail

urlpatterns = patterns(
    '',
    url(r'^$', NationList.as_view(), name="nation_list"),
    url(r'^(?P<slug>[\w-]+)/$', NationDetail.as_view(), name='nation_detail'),
)
