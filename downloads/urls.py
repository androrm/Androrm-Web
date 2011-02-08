from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('androrm.downloads.views',
    url(r'^$', 'index', name = 'download_index'),
    url(r'^license/$', 'license', name = "download_license"),
    url(r'^latest/$', 'latest', name = 'download_latest'),
    url(r'^latest/tarball/$', 'download_latest', name = 'download_latest_tarball'),
    url(r'^release/(?P<version>(\d+)(.(\d+))+)/$', 'release', name = 'download_release'),
    url(r'^release/(?P<version>(\d+)(.(\d+))+)/tarball/$', 'download_version', name = 'download_version'),
)
