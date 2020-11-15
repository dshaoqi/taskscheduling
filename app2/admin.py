from django.contrib import admin

# Register your models here.

from .models import Host,Record,User,Method,Flow,FlowMethodMembership

@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = ('ip','hostname','display_users')
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('ip', 'username')
@admin.register(Method)
class MethodAdmin(admin.ModelAdmin):
    list_display = ('ip', 'username', 'command')
admin.site.register(Record)

'''
@admin.register(Flow)
class FlowAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'create_time' )

'''

class MethodInline(admin.TabularInline):
    model = FlowMethodMembership 
    extra = 1

@admin.register(Flow)
class FlowAdmin(admin.ModelAdmin):
    inlines = (MethodInline,)
