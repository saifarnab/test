from django.contrib import admin
from django.contrib.auth.models import User, Group

from orm import models

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(models.Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ['tag', 'is_active', 'created_at']
    ordering = ['-created_at']


@admin.register(models.ConnectedAccount)
class ConnectedAccountAdmin(admin.ModelAdmin):
    list_display = ['account_name', 'email', 'reply_to', 'is_active', 'created_at']
    ordering = ['-created_at']


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'primary_email', 'is_active', 'created_at']
    ordering = ['-created_at']


@admin.register(models.SentEmail)
class SentEmailAdmin(admin.ModelAdmin):
    list_display = ['contact', 'connected_account', 'created_at']
    ordering = ['-created_at']


@admin.register(models.Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    list_display = ['config',  'max_limit_per_day', 'waiting_time']
