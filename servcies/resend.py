import json
import logging
from typing import Union

import requests
from django.conf import settings

from _applibs.email_template import get_content
from orm.models import Contact, ConnectedAccount, Template, Configuration


def _get_headers() -> dict:
    return {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {settings.RESEND_API_KEY}"
    }


def _get_resend_email_params(config: Configuration, contact: Contact, connected_acc: ConnectedAccount,
                             template: Template) -> dict:
    subject = get_content(contact, template.subject)
    email = get_content(contact, template.content)
    params = {
        "from": f"{connected_acc.account_name} <{connected_acc.email}>",
        "to": [f"{contact.primary_email}"],
        "subject": subject,
        "html": email,
        "reply_to": [connected_acc.reply_to if connected_acc.reply_to else config.primary_reply_to],
        "headers": {}
    }

    # if self.unsubscribe is not None:
    #     params["headers"]["List-Unsubscribe"] = self.unsubscribe

    return params


def send_email_via_resend(config: Configuration, contact: Contact, connected_acc: ConnectedAccount,
                          template: Template) -> Union[str, None]:
    try:
        body = _get_resend_email_params(config, contact, connected_acc, template)
        response = requests.post(settings.RESEND_API_URL, json=body, headers=_get_headers())
        return json.loads(response.content).get('id', None)
    except Exception as e:
        logging.exception(e)
        return None
