from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account


class AccountAdmin(UserAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'username', 'last_login','date_joined', 'is_active')
    list_display_links = ('email', 'id')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ('date_joined','email')
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
