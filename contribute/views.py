from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response('contribute/index.html',
                              locals(),
                              context_instance=RequestContext(request))


def donation_abort(request):
    return render_to_response('contribute/nexttime.html',
                              locals(),
                              context_instance=RequestContext(request))


def donation(request):
    return render_to_response('contribute/thankyou.html',
                              locals(),
                              context_instance=RequestContext(request))
