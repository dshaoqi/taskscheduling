from django.contrib import admin

# Register your models here.

from .models import Host,Record,User,Method,Flow

#admin.site.register(Host)
@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = ('ip','hostname','display_users')
admin.site.register(User)
admin.site.register(Method)
admin.site.register(Record)
admin.site.register(Flow)
'''
class MethodInline(admin.TabularInline):
    model = Method

@admin.register(Flow)
class FlowAdmin(admin.ModelAdmin):
    inlines = [ MethodInline ]
'''

