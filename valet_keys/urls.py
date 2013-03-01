from django.conf.urls.defaults import *

urlpatterns = patterns('valet_keys.views',
    url(r'^$', 'list', name='valet_keys.list'),
    url(r'^new$', 'new', name='valet_keys.new'),
    url(r'^(?P<pk>\d+)/history$', 'history', name='valet_keys.history'),
    url(r'^(?P<pk>\d+)/disable$', 'disable', name='valet_keys.disable'),
)
