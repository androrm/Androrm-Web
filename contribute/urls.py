from django.conf.urls import patterns, url, include

urlpatterns = patterns('androrm.contribute.views',
    url(r'^$', 'index', name='contribute_index'),
    url(r'^nexttime/$', 'donation_abort', name='donation_abort'),
    url(r'^thankyou/$', 'donation', name='donation'),
)
