from androrm import settings

def page_conf(context):
    return {
        'MEDIA_URL': settings.MEDIA_URL,
        'DEBUG': settings.DEBUG
    }