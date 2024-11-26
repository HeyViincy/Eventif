from django.test import TestCase
from django.core import mail
from contact.Forms import ContactForm

#Testes pro carregamento da página de contato
class ContactGet(TestCase): 
    def setUp(self):
        self.response = self.client.get('/contact/')

    #Verificando se a página carregou com sucesso.
    def test_Get(self):
        self.assertEqual(200, self.response.status_code)
    
    #Verificando se a página usa o template correto.
    def test_TemplateUsed(self):
        self.assertTemplateUsed(
            self.response, 'contact/contact_form.html')

    #Conferindo campos do formulário no HTML.
    def test_FormHTML(self):
        Inputs = (
            ('<form', 1),
            ('<input', 5),
            ('<textarea', 1),
            ('type="text"', 2),
            ('type="email"', 1),
            ('type="submit"', 1)
        )
        for Element, Num in Inputs:
            with self.subTest():
                self.assertContains(self.response, Element, Num)

    #Conferindo tag CSRF
    def test_CSRF(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

#Testes para o formulário no Forms
class ContactForms(TestCase):
    def setUp(self):
        self.form = ContactForm()

    #Conferindo campos do formulário no Forms
    def test_FormFields(self):
        Fields = ['name', 'phone', 'email', 'message']
        self.assertSequenceEqual(Fields, list(self.form.fields))