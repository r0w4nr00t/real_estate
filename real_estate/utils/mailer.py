""" 
Utitlity functions for sending emails in the system
Makes use of the mailtrap.io api to test, send and control emails 
"""
import mailtrap as mt
from django.conf import settings

def send_welcome_message(to,receiver_name, activation_token):
    mail = mt.MailFromTemplate(
        sender=mt.Address(email="hello@demomailtrap.com", name="Mailtrap Test"),
        to=[mt.Address(email="r0w4nr00t@gmail.com")],
        template_uuid=settings.WELCOME_TEMPLATE_ID,
        template_variables={
        "company_info_name": settings.COMPANY_NAME,
        "name": receiver_name,
        "company_info_address": settings.COMPANY_ADDRESS,
        "company_info_city": settings.CITY,
        "company_info_zip_code": settings.ZIPCODE,
        "company_info_country": settings.COUNTRY
        }
    )

    client = mt.MailtrapClient(token=settings.MAILTRAP_API_TOKEN)
    response = client.send(mail)
    if response['success']:
        return response

    return {'success':False, 'id':None}
