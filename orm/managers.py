import time
from datetime import datetime

from django.db import models
from django.utils import timezone


class TemplateManager(models.Manager):
    def get_active_email_variants(self):
        return self.filter(is_active=True).order_by('-created_at')


class ConnectedAccountManager(models.Manager):
    def get_active_accounts(self):
        return self.filter(is_active=True).order_by('-created_at')


class ContactManager(models.Manager):
    def get_active_contacts(self):
        return self.filter(is_active=True).order_by('-created_at')


class SentEmailManager(models.Manager):
    def get_total_email_count_day(self, email: str) -> int:
        return self.filter(connected_account__email=email, created_at__date=datetime.now().date()).count()

    def save_sent_email(self, template, contact, connected_account, resend_id, email_content):
        return self.create(template=template, contact=contact, connected_account=connected_account, resend_id=resend_id,
                           email_content=email_content)

    def save_followup_email(self, template, contact, connected_account, resend_id, email_content):
        return self.create(followup_template=template, contact=contact, connected_account=connected_account, resend_id=resend_id,
                           email_content=email_content, is_followup=True)

    def get_via_resend_id(self, resend_id: str):
        return self.filter(resend_id=resend_id).last()

    def get_emails_need_to_send_followup_email(self):
        return self.filter(email_complained=False, email_bounced=False, is_followup=False)

    def get_followup_email(self, followup_template, contact, connected_account):
        return self.filter(followup_template=followup_template, contact=contact, connected_account=connected_account).last()

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


class FollowUpEmailManager(models.Manager):

    def get_active_followup_emails(self, email):
        return self.filter(email=email, is_active=True).order_by('wait_for')
