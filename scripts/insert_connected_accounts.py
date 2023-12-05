"""
python3 manage.py runscript insert_connected_accounts
RES: Insert connected accounts
"""
import logging
import pandas as pd
from django.conf import settings

from orm.models import ConnectedAccount


def run():
    try:
        df = pd.read_csv(f'{settings.BASE_DIR}/resources/connected_accounts.csv', dtype=str)
        df = df.fillna('')
        df = df[['account_name', 'email', 'reply_to', 'created_date']]
        accounts = []
        for index, row in df.iterrows():
            accounts.append(
                ConnectedAccount(
                    account_name=row['account_name'],
                    email=row['email'],
                    reply_to=row['reply_to']
                )
            )

        ConnectedAccount.objects.bulk_create(accounts, batch_size=1000)
        logging.info('Execution done!')

    except Exception as err:
        logging.exception(err)
