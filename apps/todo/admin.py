from django.contrib import admin
from .models import *


class TodoAmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'priority', 'is_finished')
    readonly_fields = ('created_at',)


admin.site.register(Todo, TodoAmin)
