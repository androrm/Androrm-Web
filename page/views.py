from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from androrm.downloads.models import Release
from androrm.page.models import Entry


def index(request):
    release = Release.objects.all().order_by("-version")[0:1]

    entries = Entry.objects.filter(published=True).order_by("-date")
    paginator = Paginator(entries, 10)

    page = request.GET.get("page")

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)


    if release:
        version = release[0].version

    return render_to_response('index.html',
                              locals(),
                              context_instance=RequestContext(request))
