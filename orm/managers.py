from django.db import models
from django.utils import timezone


class TemplateManager(models.Manager):
    def get_active_templates(self):
        return self.filter(is_active=True).order_by('-created_at')


class ConnectedAccountManager(models.Manager):
    def get_active_accounts(self):
        return self.filter(is_active=True).order_by('-created_at')


class ContactManager(models.Manager):
    def get_active_contacts(self):
        return self.filter(is_active=True).order_by('-created_at')


class SentEmailManager(models.Manager):
    def get_total_email_count_day(self, email: str) -> int:
        return self.filter(connected_account__email=email, created_at__date=timezone.now().date()).count()

    def save_sent_email(self, template, contact, connected_account, resend_id, email_content):
        return self.create(template=template, contact=contact, connected_account=connected_account, resend_id=resend_id,
                           email_content=email_content)

    def get_via_resend_id(self, resend_id: str):
        return self.filter(resend_id=resend_id).last()


class EmailStatusManager(models.Manager):

    def email_status_init(self, email):
        self.create(email=email)

    def update_status(self, email, event_type: str):

        obj = self.filter(email=email).last()
        if obj:
            if event_type == 'email.sent':
                obj.email_sent = True
            elif event_type == 'email.delivered':
                obj.email_delivered = True
            elif event_type == 'email.complained':
                obj.email_complained = True
            elif event_type == 'email.delivered':
                obj.email_delivered = True
            elif event_type == 'email.bounced':
                obj.email_bounced = True
            elif event_type == 'email.opend':
                obj.email_opened = True
            elif event_type == 'email.clicked':
                obj.email_clicked = True

            obj.save()


class ConfigurationManager(models.Manager):
    def get_config(self):
        return self.get()
