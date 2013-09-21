from django.conf.urls import patterns, url, include

urlpatterns = patterns('androrm.page.views',
    url(r'^$', 'index', name = 'index'),
)
