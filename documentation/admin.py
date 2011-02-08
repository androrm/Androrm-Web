from django.contrib import admin

from androrm.documentation import models

class FunctionParamsInline(admin.TabularInline):
    model = models.Param
    extra = 1
    
class FunctionDescriptorsInline(admin.TabularInline):
    model = models.FunctionDescriptor
    extra = 1
    
class ClassDescriptorsInline(admin.TabularInline):
    model = models.ClassDescriptor
    extra = 1
    
class FunctionAdmin(admin.ModelAdmin):
    inlines = (FunctionParamsInline, FunctionDescriptorsInline)
    
class ParamAdmin(admin.ModelAdmin):
    inlines = (FunctionParamsInline,)
    
class ClassAdmin(admin.ModelAdmin):
    inlines = (ClassDescriptorsInline,)

admin.site.register(models.ClassDescription, ClassAdmin)
admin.site.register(models.FunctionDescription, FunctionAdmin)
admin.site.register(models.ParamDescription, ParamAdmin)
admin.site.register(models.Type)
admin.site.register(models.TypeDescriptor)
admin.site.register(models.Param)