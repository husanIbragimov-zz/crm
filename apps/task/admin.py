from django.contrib import admin
from .models import Task, Comment, SendTask


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'id',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Task, TaskAdmin)
admin.site.register(Comment)
admin.site.register(SendTask)
