from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone

from orm.managers import (
    TemplateManager,
    ConnectedAccountManager,
    ContactManager,
    SentEmailManager,
    ConfigurationManager, FollowUpEmailManager
)


class EmailVariant(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    tag = models.CharField(max_length=100, unique=True, blank=False, null=False)
    subject = models.CharField(max_length=1500, null=False, blank=False)
    content = RichTextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    objects = TemplateManager()

    class Meta:
        verbose_name = 'Email Variant'
        verbose_name_plural = 'Email Variants'

    def __str__(self):
        return self.title


class FollowUpEmail(models.Model):
    email = models.ForeignKey(to=EmailVariant, null=False, blank=False, on_delete=models.DO_NOTHING)
    content = RichTextField()
    wait_for = models.PositiveSmallIntegerField(default=1,
                                                help_text=f'this followup email will wait specified '
                                                          f'day from the original email')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    objects = FollowUpEmailManager()

    class Meta:
        verbose_name = 'FollowUp Email'
        verbose_name_plural = 'FollowUp Emails'

    def __str__(self):
        return self.email.title


class ConnectedAccount(models.Model):
    account_name = models.CharField(max_length=250, null=False, blank=False)
    email = models.CharField(max_length=500, null=False, blank=False)
    reply_to = models.CharField(max_length=500, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    objects = ConnectedAccountManager()

    class Meta:
        verbose_name = 'Connected Account'
        verbose_name_plural = 'Connected Accounts'

    def __str__(self):
        return self.account_name


class Contact(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    primary_phone = models.CharField(max_length=250, null=True, blank=True)
    other_phones = models.CharField(max_length=250, null=True, blank=True)
    primary_email = models.CharField(max_length=250, null=True, blank=True)
    other_emails = models.CharField(max_length=250, null=True, blank=True)
    linkedin_profile = models.CharField(max_length=250, null=True, blank=True)
    custom_first_phone = models.CharField(max_length=250, null=True, blank=True)
    date_created = models.CharField(max_length=250, null=True, blank=True)
    lead_id = models.CharField(max_length=250, null=True, blank=True)
    lead_display_name = models.CharField(max_length=250, null=True, blank=True)
    lead_url = models.CharField(max_length=250, null=True, blank=True)
    lead_status_label = models.CharField(max_length=250, null=True, blank=True)
    lead_custom_company_address = models.CharField(max_length=250, null=True, blank=True)
    lead_custom_company_city = models.CharField(max_length=250, null=True, blank=True)
    lead_custom_company_country = models.CharField(max_length=250, null=True, blank=True)
    lead_custom_company_description = models.CharField(max_length=2500, null=True, blank=True)
    lead_custom_company_industry = models.CharField(max_length=250, null=True, blank=True)
    lead_custom_company_li_profile = models.CharField(max_length=250, null=True, blank=True)
    lead_custom_company_linkedin = models.CharField(max_length=250, null=True, blank=True)
    lead_custom_company_phone = models.CharField(max_length=250, null=True, blank=True)
    lead_custom_company_phone1 = models.CharField(max_length=250, null=True, blank=True)
    lead_custom_company_state = models.CharField(max_length=250, null=True, blank=True)
    lead_custom_contact_city = models.CharField(max_length=250, null=True, blank=True)
    lead_custom_contact_job_title = models.CharField(max_length=250, null=True, blank=True)
    lead_custom_contact_li_profile_url = models.CharField(max_length=250, null=True, blank=True)
    lead_custom_contact_linkedin_profile = models.CharField(max_length=250, null=True, blank=True)
    lead_custom_contact_location = models.CharField(max_length=250, null=True, blank=True)
    lead_custom_contact_phone_number = models.CharField(max_length=250, null=True, blank=True)
    lead_custom_contact_state = models.CharField(max_length=250, null=True, blank=True)
    lead_custom_corporate_phone = models.CharField(max_length=250, null=True, blank=True)
    lead_custom_person_assigned = models.CharField(max_length=250, null=True, blank=True)
    lead_custom_person_linkedin_url = models.CharField(max_length=250, null=True, blank=True)
    lead_html_url = models.CharField(max_length=250, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_unsubscribe = models.BooleanField(default=False)
    unsubscribe_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    objects = ContactManager()

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name


class SentEmail(models.Model):
    template = models.ForeignKey(to=EmailVariant, null=True, blank=True, on_delete=models.DO_NOTHING)
    followup_template = models.ForeignKey(to=FollowUpEmail, null=True, blank=True, on_delete=models.DO_NOTHING)
    contact = models.ForeignKey(to=Contact, null=False, blank=False, on_delete=models.DO_NOTHING)
    connected_account = models.ForeignKey(to=ConnectedAccount, null=False, blank=False, on_delete=models.DO_NOTHING)
    resend_id = models.CharField(max_length=250, null=True, blank=True)
    email_content = models.TextField(null=True, blank=True)
    email_sent = models.BooleanField(default=False)
    email_delivered = models.BooleanField(default=False)
    email_complained = models.BooleanField(default=False)
    email_bounced = models.BooleanField(default=False)
    email_opened = models.BooleanField(default=False)
    email_clicked = models.BooleanField(default=False)
    is_followup = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    objects = SentEmailManager()

    class Meta:
        verbose_name = 'Sent Email'
        verbose_name_plural = 'Sent Emails'

    def __str__(self):
        return self.contact.name


class Configuration(models.Model):
    config = models.CharField(max_length=100, default='Config', editable=False)
    contact_pointer = models.IntegerField(default=0)
    max_limit_per_day = models.IntegerField(default=50, help_text='maximum email send limit from an account')
    waiting_time = models.IntegerField(default=1, help_text='waiting time in minutes')
    primary_reply_to = models.CharField(max_length=250, null=True, blank=True, help_text='primary reply to email')

    objects = ConfigurationManager()

    class Meta:
        verbose_name = 'Configuration'
        verbose_name_plural = 'Configuration'

    def __str__(self):
        return self.config
