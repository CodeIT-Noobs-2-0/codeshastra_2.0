from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User

# Register your models here.

class BaseUserAdmin(UserAdmin):
    list_display = ['email', 'is_admin', 'is_donor', 'is_ngo_admin']
    search_fields = ("email", 'is_admin', 'is_donor', 'is_ngo_admin')
    exclude = []
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ['email']



admin.site.site_header = 'Codeshastra 7.0'
admin.site.site_title = 'Catch 22'
admin.site.index_title = 'Site admin panel'
admin.site.unregister(Group)
admin.site.register(User)