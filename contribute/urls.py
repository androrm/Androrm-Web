from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('androrm.contribute.views',
    url(r'^$', 'index', name = 'contribute_index'),
)
