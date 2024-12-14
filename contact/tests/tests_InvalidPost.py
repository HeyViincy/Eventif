from django.test import TestCase
from contact.Forms import ContactForm
from contact.models import Contact

#Testes para um post inválido.
class InvalidPost(TestCase):
    def setUp(self):
        self.response = self.client.post('/contact/', {})
    
    #Verificando se o response é recarregar a página.
    def test_PostResp(self):
        self.assertEqual(200, self.response.status_code)
    
    #Conferindo se carrega o template correto.
    def test_TemplateUsed(self):
        self.assertTemplateUsed(self.response, 'contact/contact_form.html')

    #Conferindo formulário na resposta.
    def test_FormCheck(self):
        Form = self.response.context['form']
        self.assertIsInstance(Form, ContactForm)

    #Conferindo se há erros no envio.
    def test_FormErrors(self):
        Form = self.response.context['form']
        self.assertTrue(Form.errors)

    #Conferindo se o contato não é registrado no banco de dados.
    def test_CancelSave(self):
        self.assertFalse(Contact.objects.exists())