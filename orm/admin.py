from django.contrib import admin
from django.conf import settings
from django.contrib.auth.models import User, Group

from orm import models

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(models.EmailVariant)
class EmailVariantAdmin(admin.ModelAdmin):
    list_display = ['title', 'tag', 'is_active', 'created_at']
    ordering = ['-created_at']


@admin.register(models.FollowUpEmail)
class FollowUpEmailAdmin(admin.ModelAdmin):
    list_display = ['email', 'wait_for', 'is_active', 'created_at']
    ordering = ['-created_at']


@admin.register(models.ConnectedAccount)
class ConnectedAccountAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True if settings.STAGE in ['development', 'uat'] else False

    def has_delete_permission(self, request, obj=None):
        return True if settings.STAGE in ['development', 'uat'] else False

    def has_change_permission(self, request, obj=None):
        return True if settings.STAGE in ['development', 'uat'] else False

    list_display = ['account_name', 'email', 'reply_to', 'is_active', 'created_at']
    ordering = ['-created_at']


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True if settings.STAGE in ['development', 'uat'] else False

    def has_delete_permission(self, request, obj=None):
        return True if settings.STAGE in ['development', 'uat'] else False

    def has_change_permission(self, request, obj=None):
        return True if settings.STAGE in ['development', 'uat'] else False

    list_display = ['name', 'primary_email', 'is_active', 'created_at']
    ordering = ['-created_at']


@admin.register(models.SentEmail)
class SentEmailAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True if settings.STAGE in ['development', 'uat'] else False

    def has_delete_permission(self, request, obj=None):
        return True if settings.STAGE in ['development', 'uat'] else False

    def has_change_permission(self, request, obj=None):
        return True if settings.STAGE in ['development', 'uat'] else False

    list_display = ['contact', 'connected_account', 'resend_id', 'created_at']
    ordering = ['-created_at']


@admin.register(models.Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True if settings.STAGE in ['development', 'uat'] else False

    def has_delete_permission(self, request, obj=None):
        return True if settings.STAGE in ['development', 'uat'] else False

    def has_change_permission(self, request, obj=None):
        return True if settings.STAGE in ['development', 'uat'] else False

    list_display = ['config', 'contact_pointer', 'waiting_time', 'max_limit_per_day']
