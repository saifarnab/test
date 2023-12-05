"""
python3 manage.py runscript send_email
RES: Send email periodically
"""
import logging
import time

from orm.models import ConnectedAccount, Contact, Configuration, SentEmail, Template
from servcies.resend import send_email_via_resend


def _email_sender(self, connected_accounts: [ConnectedAccount], contacts: [Contact]):
    # get data
    config = self.get_config()
    template = Template.objects.filter().last()
    pointer = config.pointer

    while True:
        if pointer >= len(contacts):
            break

        for connected_account in connected_accounts:
            if pointer >= len(contacts):
                break

            if SentEmail.objects.get_total_email_count_day(connected_account.email) > config.max_limit_per_day:
                logging.info(f'This email {connected_account.email} reach the max limit of sending email in a day')
                continue

            # select contact from pointer value
            contact = contacts[config.pointer]

            # send email via resend
            resend_id = send_email_via_resend(config, contact, connected_account, template)
            if not resend_id:
                logging.error('email sent unsuccessful')
                pointer += 1
                continue

            # insert email in db
            email = SentEmail.objects.insert(template, contact, connected_account, resend_id)
            if not email:
                logging.error('email sent successfully but failed to insert in DB')

            pointer += 1
            logging.info(f'email successfully send to {contact.name}')

        # update pointer value
        config.pointer = pointer
        config.save()

        logging.info(f'waiting for {config.waiting_time} seconds to start sending emails')
        time.sleep(config.waiting_time)


def run():
    try:
        contacts = Contact.objects.get_active_contacts()
        connected_accounts = ConnectedAccount.objects.get_active_accounts()
        config = Configuration.objects.get_config()

        _email_sender(config, connected_accounts, contacts)

        logging.info("successfully send email to all the contacts")

    except Exception as err:
        logging.exception(err)
