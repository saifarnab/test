"""
python3 manage.py runscript send_emails
RES: Send email periodically
"""
import logging
import time

from _applibs.utils import reset_template_counter, total_counter
from orm.models import ConnectedAccount, Contact, Configuration, SentEmail, EmailVariant
from servcies.resend import send_email_via_resend


def _email_sender(config: Configuration, email_variants: [EmailVariant], connected_accounts: [ConnectedAccount],
                  contacts: [Contact]):
    # set required pointers
    pointer = config.contact_pointer
    template_pointer = 0
    total_template_count, total_contact_count, total_connected_account_count = total_counter(email_variants, contacts,
                                                                                             connected_accounts)
    if total_template_count < 1 or total_contact_count < 1 or total_connected_account_count < 1:
        logging.info('no templates/contacts/connected_accounts available to proceed!')
        return

    # process initiate
    while True:
        if pointer >= total_contact_count:
            break

        for connected_account in connected_accounts:
            if pointer >= total_contact_count:
                break

            if SentEmail.objects.get_total_email_count_day(connected_account.email) >= config.max_limit_per_day:
                logging.info(f'This email {connected_account.email} reach the max limit of sending email in a day')
                continue

            # select contact from pointer value
            contact = contacts[config.contact_pointer]

            # send email via resend
            resend_id, content = send_email_via_resend(config, contact, connected_account, email_variants[template_pointer])
            if not resend_id:
                logging.error('email sent unsuccessful')
                pointer += 1
                continue

            # insert email in db
            sent_email = SentEmail.objects.save_sent_email(email_variants[template_pointer], contact, connected_account,
                                                           resend_id, content)
            if not sent_email:
                logging.error('email sent successfully but failed to insert in DB')

            # reset pointers
            pointer += 1
            template_pointer = reset_template_counter(template_pointer, total_template_count)
            logging.info(f'email successfully send to {contact.name}')

        # update pointer value
        config.contact_pointer = pointer
        config.save()

        logging.info(f'Waiting for {config.waiting_time*60} seconds to start sending emails')
        time.sleep(config.waiting_time*60)


def run():
    try:
        config = Configuration.objects.get_config()
        templates = EmailVariant.objects.get_active_email_variants()
        contacts = Contact.objects.get_active_contacts()
        connected_accounts = ConnectedAccount.objects.get_active_accounts()
        _email_sender(config, templates, connected_accounts, contacts)
        logging.info("successfully send email to all the contacts")

    except Exception as err:
        logging.exception(err)
