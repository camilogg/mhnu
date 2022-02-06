from celery import shared_task
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _

from utils.tasks import send_mail_task


@shared_task
def send_mail_contact(names: str, subject: str, email: str, message: str):
    title = _('Contact email')
    msg_html = render_to_string('museum/contact_email.html', {
        'names': names,
        'subject': subject,
        'message': message,
        'email': email
    })
    send_mail_task(settings.EMAIL_HOST_USER, title, msg_html)
