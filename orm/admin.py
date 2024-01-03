from django.contrib import admin
from django.conf import settings
from django.contrib.auth.models import User, Group
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from bs4 import BeautifulSoup

from orm import models

admin.site.unregister(User)
admin.site.unregister(Group)


class EmailForm(forms.ModelForm):
    class Meta:
        model = models.EmailVariant
        fields = '__all__'
        widgets = {
            'tag': FilteredSelectMultiple("Multi Select Field", is_stacked=False),
        }


@admin.register(models.EmailVariant)
class EmailVariantAdmin(admin.ModelAdmin):
    form = EmailForm
    list_display = ['title', 'subject', 'is_active', 'created_at']
    search_fields = ['title', 'subject']
    ordering = ['-created_at']

    def save_model(self, request, obj, form, change):
        soup = BeautifulSoup(obj.subject, 'html.parser')
        obj.subject = soup.get_text()
        super().save_model(request, obj, form, change)


@admin.register(models.FollowUpEmail)
class FollowUpEmailAdmin(admin.ModelAdmin):
    form = EmailForm
    search_fields = ['title', 'subject']
    list_display = ['title', 'subject', 'wait_for', 'is_active', 'created_at']
    ordering = ['-created_at']

    def save_model(self, request, obj, form, change):
        soup = BeautifulSoup(obj.subject, 'html.parser')
        obj.subject = soup.get_text()
        super().save_model(request, obj, form, change)


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

    list_display = ['contact', 'connected_account', 'resend_id', 'is_followup', 'created_at']
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
