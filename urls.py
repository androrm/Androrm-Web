from django.conf.urls.defaults import *

from androrm import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', include('androrm.page.urls')),
    (r'^documentation/', include('androrm.documentation.urls')),
    (r'^downloads/', include('androrm.downloads.urls')),
    (r'^contribute/', include('androrm.contribute.urls')),
    
    # delete for production
    #(r'^src/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': settings.MEDIA_ROOT}),
)
