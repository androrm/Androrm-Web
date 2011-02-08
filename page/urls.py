from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('androrm.page.views',
    url(r'^$', 'index', name = 'index'),
)
