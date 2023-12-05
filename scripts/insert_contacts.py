"""
python3 manage.py runscript insert_contacts
RES: Insert contacts
"""
import logging
import pandas as pd
from django.conf import settings

from orm.models import ConnectedAccount, Contact


def run():
    try:
        df = pd.read_csv(f'{settings.BASE_DIR}/resources/contacts.csv', dtype=str)
        df = df.fillna('')
        df = df[['name', 'first_name', 'last_name', 'title', 'primary_phone', 'other_phones', 'primary_email',
                 'other_emails', 'custom.Contact LinkedIn Profile', 'custom.First Phone', 'date_created', 'lead_id',
                 'lead_display_name', 'lead_url', 'lead_status_label', 'lead_custom.Company Address',
                 'lead_custom.Company City', 'lead_custom.Company Country', 'lead_custom.Company Description',
                 'lead_custom.Company Industry', 'lead_custom.Company LI Profile Url', 'lead_custom.Company LinkedIn',
                 'lead_custom.Company Phone', 'lead_custom.Company Phone 1', 'lead_custom.Company State',
                 'lead_custom.Contact City', 'lead_custom.Contact Job Title', 'lead_custom.Contact LI Profile URL',
                 'lead_custom.Contact LinkedIn Profile', 'lead_custom.Contact Location',
                 'lead_custom.Contact Phone Number', 'lead_custom.Contact State', 'lead_custom.Corporate Phone',
                 'lead_custom.Person Assigned', 'lead_custom.Person Linkedin Url', 'lead_html_url']]
        contacts = []
        for index, row in df.iterrows():
            contacts.append(
                Contact(
                    name=row['name'], first_name=row['first_name'], last_name=row['last_name'], title=row['title'],
                    primary_phone=row['primary_phone'],
                    other_phones=row['other_phones'],
                    primary_email=row['primary_email'], other_emails=row['other_emails'], linkedin_profile=row['custom.Contact LinkedIn Profile'],
                    custom_first_phone=row['custom.First Phone'],
                    date_created=row['date_created'], lead_id=row['lead_id'], lead_display_name=row['lead_display_name'], lead_url=row['lead_url'],
                    lead_status_label=row['lead_status_label'],
                    lead_custom_company_address=row['lead_custom.Company Address'], lead_custom_company_city=row['lead_custom.Company City'],
                    lead_custom_company_country=row['lead_custom.Company Country'],
                    lead_custom_company_description=row['lead_custom.Company Description'], lead_custom_company_industry=row['lead_custom.Company Industry'],
                    lead_custom_company_li_profile=row['lead_custom.Company LI Profile Url'], lead_custom_company_linkedin=row['lead_custom.Company LinkedIn'],
                    lead_custom_company_phone=row['lead_custom.Company Phone'], lead_custom_company_phone1=row['lead_custom.Company Phone 1'],
                    lead_custom_company_state=row['lead_custom.Company State'],
                    lead_custom_contact_city=row['lead_custom.Contact City'], lead_custom_contact_job_title=row['lead_custom.Contact Job Title'],
                    lead_custom_contact_li_profile_url=row['lead_custom.Contact LI Profile URL'],
                    lead_custom_contact_linkedin_profile=row['lead_custom.Contact LinkedIn Profile'], lead_custom_contact_location=row['lead_custom.Contact Location'],
                    lead_custom_contact_phone_number=row['lead_custom.Contact Phone Number'],
                    lead_custom_contact_state=row['lead_custom.Contact State'], lead_custom_corporate_phone=row['lead_custom.Corporate Phone'],
                    lead_custom_person_assigned=row['lead_custom.Person Assigned'],
                    lead_custom_person_linkedin_url=row['lead_custom.Person Linkedin Url'], lead_html_url=row['lead_html_url']
                )
            )

        Contact.objects.bulk_create(contacts, batch_size=1000)
        logging.info('Execution done!')

    except Exception as err:
        logging.exception(err)
