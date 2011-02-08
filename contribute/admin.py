from django.contrib import admin

from androrm.contribute import models

admin.site.register(models.BugReport)
admin.site.register(models.FeatureRequest)
admin.site.register(models.User)
admin.site.register(models.Comment)