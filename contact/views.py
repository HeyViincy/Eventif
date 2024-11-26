from django.shortcuts import render
from contact.Forms import ContactForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.core import mail
from django.conf import settings

def _SendEmail(Template, Data, From, To):
    EmailBody = render_to_string(Template, Data)
    mail.send_mail("Contato Recebido", EmailBody, From, [From, To])

def FormPost(request):
    Form = ContactForm(request.POST)
    if not Form.is_valid():
        return render(request, 'contact/contact_form.html', {'form': Form})
    _SendEmail(
        'contact/contact_email.txt',
        Form.cleaned_data,
        Form.cleaned_data["email"],
        settings.DEFAULT_FROM_EMAIL
    )
    messages.success(request, 'Sua mensagem foi enviada! Responderemos em breve!')
    return HttpResponseRedirect('/contact/')

def Contact(request):
    if request.method == 'POST':
        return FormPost(request)
    else:
        return render(request, 'contact/contact_form.html', {'form': ContactForm()})