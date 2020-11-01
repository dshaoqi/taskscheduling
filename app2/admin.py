from django.contrib import admin

# Register your models here.

from .models import Host,Record,User,Method

admin.site.register(Host)
admin.site.register(User)
admin.site.register(Method)
admin.site.register(Record)
