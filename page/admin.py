from django.contrib import admin

from androrm.page import models

admin.site.register(models.Category)
admin.site.register(models.Entry)
admin.site.register(models.Author)