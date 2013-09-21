from django.conf.urls import patterns, url

urlpatterns = patterns('androrm.documentation.views',
    url(r'^$', 'index', name = 'documentation_index'),
    url(r'^models/$', 'models', name = 'documentation_models'),
    url(r'^models/migrations/$', 'migrations', name = 'documentation_migrations'),
    url(r'^models/field_types/$', 'fields', name = 'documentation_fields'),
    url(r'^models/field_types/data_fields/$', 'data_fields', name = "documentation_data_fields"),
    url(r'^models/field_types/relational_fields/$', 'relational_fields', name = 'documentation_relational_fields'),
    url(r'^queries/$', 'queries', name = "documentation_making_queries"),
    url(r'^beginners/$', 'beginners', name = 'documentation_beginners'),
    url(r'^beginners/kick-start/$', 'kick_start', name = 'documentation_kick_start'),
    url(r'^beginners/installation/$', 'installation', name = 'documentation_installation'),
    url(r'^beginners/tutorials/$', 'tutorials', name = 'documentation_tutorials'),
    url(r'^beginners/tutorials/part/(?P<part>\d+)/$', 'tutorial', name = "documentation_tutorial"),
)
