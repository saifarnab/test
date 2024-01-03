"""
python3 manage.py runscript send_followup_emails
RES: Send email periodically
"""
import datetime
import logging

from orm.models import Configuration, SentEmail, FollowUpEmail
from servcies.resend import send_followup_email_via_resend


def _get_followup_email(followup_emails: [FollowUpEmail], original_email_date: datetime) -> [FollowUpEmail, None]:
    for followup_email in followup_emails:
        cal_time = (original_email_date + datetime.timedelta(days=followup_email.wait_for)).date()
        # print(cal_time, datetime.datetime.now().date(), original_email_date, followup_email.wait_for)
        if cal_time <= datetime.datetime.now().date():
            return followup_email
    return None


def _followup_email_sender(config: Configuration):
    # get original emails
    emails = SentEmail.objects.get_emails_need_to_send_followup_email()
    if not emails:
        logging.info(f'no followup emails to send')
        return

    for email in emails:

        # get original emails
        followup_emails = FollowUpEmail.objects.get_active_followup_emails(email.template)
        if not followup_emails:
            logging.info(f'no followup emails to send')
            continue
        followup_email = _get_followup_email(followup_emails, email.created_at)
        if not followup_email:
            logging.info(f'followup email does not match condition to send to {email.contact.name}')
            continue

        # check already sent a followup email
        if SentEmail.objects.get_followup_email(followup_email, email.contact, email.connected_account):
            logging.info('already sent this followup email ...')
            continue

        # send email via resend
        resend_id, content = send_followup_email_via_resend(config, email.contact, email.connected_account,
                                                            followup_email)
        if not resend_id:
            logging.info(f'followup email unsuccessful send to {email.contact.name}')
            continue

        # insert email in db
        _ = SentEmail.objects.save_followup_email(followup_email, email.contact, email.connected_account,
                                                  resend_id, content)

        logging.info(f'followup email successfully send to {email.contact.name}')


def run():
    try:
        config = Configuration.objects.get_config()
        _followup_email_sender(config)

    except Exception as err:
        logging.exception(err)
