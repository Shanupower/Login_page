from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User, NewsModel
admin.site.unregister(Group,)

class userAdmin(UserAdmin):
    search_fields = ('email', 'first_name','last_name')
    list_filter = ('is_active', 'is_staff')
    ordering = ('-date_joined',)
    list_display = ('email','is_active', 'is_staff')
    readonly_fields=('last_login',)
    fieldsets = (
        ('Personal', {'fields': ('first_name','last_name','email','password')}),
        ('Security', {'fields': ('last_ip_address', 'last_login')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_admin', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )

admin.site.register(User, userAdmin)
admin.site.register(NewsModel)