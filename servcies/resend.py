import json
import logging
import random
import time
from typing import Union

import requests
from django.conf import settings

from _applibs.email_template import get_content
from orm.models import Contact, ConnectedAccount, EmailVariant, Configuration, FollowUpEmail


def _get_headers() -> dict:
    return {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {settings.RESEND_API_KEY}"
    }


def _get_resend_email_params(config: Configuration, contact: Contact, connected_acc: ConnectedAccount,
                             email_variant: EmailVariant) -> dict:
    subject = get_content(contact, email_variant.subject)
    email = get_content(contact, email_variant.content)
    params = {
        "from": f"{connected_acc.account_name} <{connected_acc.email}>",
        "to": [f"{contact.primary_email}"],
        "subject": subject,
        "html": email,
        "reply_to": connected_acc.reply_to if connected_acc.reply_to not in [None, ''] else '',
        "headers": {}
    }

    # if self.unsubscribe is not None:
    #     params["headers"]["List-Unsubscribe"] = self.unsubscribe

    return params


def _get_resend_followup_email_params(config: Configuration, contact: Contact, connected_acc: ConnectedAccount,
                                      followup_email: FollowUpEmail) -> dict:
    subject = get_content(contact, followup_email.email.subject)
    email = get_content(contact, followup_email.content)
    params = {
        "from": f"{connected_acc.account_name} <{connected_acc.email}>",
        "to": [f"{contact.primary_email}"],
        "subject": subject,
        "html": email,
        "reply_to": connected_acc.reply_to if connected_acc.reply_to not in [None, ''] else '',
        "headers": {}
    }

    # if self.unsubscribe is not None:
    #     params["headers"]["List-Unsubscribe"] = self.unsubscribe

    return params


def send_email_via_resend(config: Configuration, contact: Contact, connected_acc: ConnectedAccount,
                          email_variant: EmailVariant) -> (Union[str, None], str):
    try:
        body = _get_resend_email_params(config, contact, connected_acc, email_variant)
        return random.randint(100000, 10000000000000).__str__(), body.get('html', '')
        # response = requests.post(settings.RESEND_API_URL, json=body, headers=_get_headers())
        # return json.loads(response.content).get('id', None), body.get('html', '')
    except Exception as e:
        logging.exception(e)
        return None


def send_followup_email_via_resend(config: Configuration, contact: Contact, connected_acc: ConnectedAccount,
                                   followup_email: FollowUpEmail) -> (Union[str, None], str):
    try:
        body = _get_resend_followup_email_params(config, contact, connected_acc, followup_email)
        return random.randint(100000, 10000000000000).__str__(), body.get('html', '')
        # response = requests.post(settings.RESEND_API_URL, json=body, headers=_get_headers())
        # return json.loads(response.content).get('id', None), body.get('html', '')
    except Exception as e:
        logging.exception(e)
        return None
