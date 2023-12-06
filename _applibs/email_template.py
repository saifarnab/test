from jinja2 import Template

from orm.models import Contact


def _generate_data(contact: Contact):
    return {
        'name': contact.name,
        'first_name': contact.first_name,
        'last_name': contact.last_name,
        'title': contact.title,
        'primary_phone': contact.primary_phone,
        'other_phones': contact.other_phones,
        'primary_email': contact.primary_email,
        'other_emails': contact.other_emails,
        'linkedin_profile': contact.linkedin_profile,
        'custom_first_phone': contact.custom_first_phone,
        'date_created': contact.date_created,
        'lead_id': contact.lead_id,
        'lead_display_name': contact.lead_display_name,
        'lead_url': contact.lead_url,
        'lead_status_label': contact.lead_status_label,
        'lead_custom_company_address': contact.lead_custom_company_address,
        'lead_custom_company_city': contact.lead_custom_company_city,
        'lead_custom_company_country': contact.lead_custom_company_country,
        'lead_custom_company_description': contact.lead_custom_company_description,
        'lead_custom_company_industry': contact.lead_custom_company_industry,
        'lead_custom_company_li_profile': contact.lead_custom_company_li_profile,
        'lead_custom_company_linkedin': contact.lead_custom_company_linkedin,
        'lead_custom_company_phone': contact.lead_custom_company_phone,
        'lead_custom_company_phone1': contact.lead_custom_company_phone1,
        'lead_custom_company_state': contact.lead_custom_company_state,
        'lead_custom_contact_city': contact.lead_custom_contact_city,
        'lead_custom_contact_job_title': contact.lead_custom_contact_job_title,
        'lead_custom_contact_li_profile_url': contact.lead_custom_contact_li_profile_url,
        'lead_custom_contact_linkedin_profile': contact.lead_custom_contact_linkedin_profile,
        'lead_custom_contact_location': contact.lead_custom_contact_location,
        'lead_custom_contact_phone_number': contact.lead_custom_contact_phone_number,
        'lead_custom_contact_state': contact.lead_custom_contact_state,
        'lead_custom_corporate_phone': contact.lead_custom_corporate_phone,
        'lead_custom_person_assigned': contact.lead_custom_person_assigned,
        'lead_custom_person_linkedin_url': contact.lead_custom_person_linkedin_url,
        'lead_html_url': contact.lead_html_url
    }


def get_content(contact: Contact, content: str) -> str:
    template = Template(content)
    return template.render(_generate_data(contact))

