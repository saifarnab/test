# Generated by Django 4.2.6 on 2024-01-03 05:33

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Configuration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "config",
                    models.CharField(default="Config", editable=False, max_length=100),
                ),
                ("contact_pointer", models.IntegerField(default=0)),
                (
                    "max_limit_per_day",
                    models.IntegerField(
                        default=50, help_text="maximum email send limit from an account"
                    ),
                ),
                (
                    "waiting_time",
                    models.IntegerField(default=1, help_text="waiting time in minutes"),
                ),
                (
                    "primary_reply_to",
                    models.CharField(
                        blank=True,
                        help_text="primary reply to email",
                        max_length=250,
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Configuration",
                "verbose_name_plural": "Configuration",
            },
        ),
        migrations.CreateModel(
            name="ConnectedAccount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("account_name", models.CharField(max_length=250)),
                ("email", models.CharField(max_length=500)),
                ("reply_to", models.CharField(max_length=500)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                "verbose_name": "Connected Account",
                "verbose_name_plural": "Connected Accounts",
            },
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=250, null=True)),
                ("first_name", models.CharField(blank=True, max_length=250, null=True)),
                ("last_name", models.CharField(blank=True, max_length=250, null=True)),
                ("title", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "primary_phone",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "other_phones",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "primary_email",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "other_emails",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "linkedin_profile",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "custom_first_phone",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "date_created",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("lead_id", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "lead_display_name",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("lead_url", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "lead_status_label",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "lead_custom_company_address",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "lead_custom_company_city",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "lead_custom_company_country",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "lead_custom_company_description",
                    models.CharField(blank=True, max_length=2500, null=True),
                ),
                (
                    "lead_custom_company_industry",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "lead_custom_company_li_profile",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "lead_custom_company_linkedin",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "lead_custom_company_phone",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "lead_custom_company_phone1",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "lead_custom_company_state",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "lead_custom_contact_city",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "lead_custom_contact_job_title",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "lead_custom_contact_li_profile_url",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "lead_custom_contact_linkedin_profile",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "lead_custom_contact_location",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "lead_custom_contact_phone_number",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "lead_custom_contact_state",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "lead_custom_corporate_phone",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "lead_custom_person_assigned",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "lead_custom_person_linkedin_url",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "lead_html_url",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_unsubscribe", models.BooleanField(default=False)),
                ("unsubscribe_date", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                "verbose_name": "Contact",
                "verbose_name_plural": "Contacts",
            },
        ),
        migrations.CreateModel(
            name="EmailVariant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("tag", models.CharField(max_length=100, unique=True)),
                ("subject", ckeditor.fields.RichTextField()),
                ("content", ckeditor.fields.RichTextField()),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                "verbose_name": "Email Variant",
                "verbose_name_plural": "Email Variants",
            },
        ),
        migrations.CreateModel(
            name="FollowUpEmail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", ckeditor.fields.RichTextField(blank=True, null=True)),
                ("content", ckeditor.fields.RichTextField()),
                (
                    "wait_for",
                    models.PositiveSmallIntegerField(
                        default=1,
                        help_text="this followup email will wait specified day from the original email",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "email",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="orm.emailvariant",
                    ),
                ),
            ],
            options={
                "verbose_name": "FollowUp Email",
                "verbose_name_plural": "FollowUp Emails",
            },
        ),
        migrations.CreateModel(
            name="SentEmail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("resend_id", models.CharField(blank=True, max_length=250, null=True)),
                ("email_content", models.TextField(blank=True, null=True)),
                ("email_sent", models.BooleanField(default=False)),
                ("email_delivered", models.BooleanField(default=False)),
                ("email_complained", models.BooleanField(default=False)),
                ("email_bounced", models.BooleanField(default=False)),
                ("email_opened", models.BooleanField(default=False)),
                ("email_clicked", models.BooleanField(default=False)),
                ("is_followup", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "connected_account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="orm.connectedaccount",
                    ),
                ),
                (
                    "contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="orm.contact"
                    ),
                ),
                (
                    "followup_template",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="orm.followupemail",
                    ),
                ),
                (
                    "template",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="orm.emailvariant",
                    ),
                ),
            ],
            options={
                "verbose_name": "Sent Email",
                "verbose_name_plural": "Sent Emails",
            },
        ),
    ]
