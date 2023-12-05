from django.db import models
from django.utils import timezone


class TemplateManager(models.Manager):
    pass


class ConnectedAccountManager(models.Manager):
    def get_active_accounts(self):
        return self.filter(is_active=True).order_by('-created_at')


class ContactManager(models.Manager):
    def get_active_contacts(self):
        return self.filter(is_active=True).order_by('-created_at')


class SentEmailManager(models.Manager):
    def get_total_email_count_day(self, email: str) -> int:
        return self.filter(connected_account__email=email, created_at__date=timezone.now().date()).count()

    def insert(self, template, contact, connected_account, resend_id):
        return self.create(template, contact, connected_account, resend_id)


class EmailStatusManager(models.Manager):
    pass


class ConfigurationManager(models.Manager):
    def get_config(self):
        self.get()
