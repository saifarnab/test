"""
python3 manage.py runscript config_init
RES: Set configuration
"""
import logging

from orm.models import Configuration


def run():
    try:
        if not Configuration.objects.filter().last():
            Configuration.objects.create()
        logging.info('Execution done!')
    except Exception as err:
        logging.exception(err)
