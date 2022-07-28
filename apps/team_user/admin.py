from django.contrib import admin
from .models import Account, Group


class AccountAmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'id')
    search_fields = ('first_name', 'last_name', 'email')
    readonly_fields = ('date_created',)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    filter_horizontal = ('user',)


admin.site.register(Group, GroupAdmin)
admin.site.register(Account, AccountAmin)

