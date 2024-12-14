from django.db.models.signals import pre_save
from django.dispatch import receiver
from contact.models import Contact
from django.template.loader import render_to_string
from django.core import mail
from django.conf import settings
from django.utils.timezone import now

@receiver(pre_save, sender=Contact)
def ContactResponse(sender, instance, **kwargs):
    if instance.response != "":
        EmailBody = render_to_string('contact/contact_response.txt', vars(instance))
        mail.send_mail('Resposta ao contato', EmailBody, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL, instance.email])
        instance.response_sent_at = now()
        instance.flag = True
    else:
        print('sem mudança, sem email')