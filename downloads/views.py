from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect

from androrm.settings import STATIC_URL
from androrm.downloads.models import Release

def index(request):
    latest_version = Release.objects.all().order_by("-date")[0:1][0].version
    releases = Release.objects.all().order_by("-version")

    return render_to_response('downloads/index.html',
                              locals(),
                              context_instance=RequestContext(request))


def latest(request):
    releases = Release.objects.all().order_by("-version")
    latest = releases[0]

    return HttpResponseRedirect(reverse("download_release", kwargs={"version": latest.version}))


def release(request, version):
    release = get_object_or_404(Release, version=version)
    releases = Release.objects.all().order_by("-version")

    latest_version = releases[0].version

    return render_to_response('downloads/release.html',
                              locals(),
                              context_instance=RequestContext(request))


def get_latest_version():
    return Release.objects.all().order_by("-date")[0:1][0].version


def download_latest_tar(request):
    return HttpResponseRedirect(reverse('download_version_tar', kwargs={"version": get_latest_version()}))


def download_latest_zip(request):
    return HttpResponseRedirect(reverse('download_version_zip', kwargs={"version": get_latest_version()}))


def download_latest_source(request):
    return HttpResponseRedirect(reverse('download_version_source', kwargs={"version": get_latest_version()}))


def download_version_tar(request, version):
    return download_version(request, version, "tar.gz")


def download_version_zip(request, version):
    return download_version(request, version, "zip")


def download_version_source(request, version):
    return HttpResponseRedirect("%sreleases/androrm.source_%s.zip" % (STATIC_URL, version))


def download_version(request, version, type):
    release = get_object_or_404(Release, version=version)

    return HttpResponseRedirect("%sreleases/androrm_%s.%s" % (STATIC_URL, version, type))


def license(request):
    latest_version = Release.objects.all().order_by("-date")[0:1][0].version

    return render_to_response("downloads/license.html",
                              locals(),
                              context_instance=RequestContext(request))
