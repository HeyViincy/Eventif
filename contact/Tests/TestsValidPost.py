from django.test import TestCase
from django.core import mail

#Testes para um post válido.
class ValidPost(TestCase):
    def setUp(self):
        #Dados para a simulação do envio.
        Data = dict(
                    name = "Vincent Moreira",
                    phone = "53-91234-5678",
                    email = "HeyViincy@gmail.com",
                    message = "Mensagem de contato"
                    )
        self.response = self.client.post('/contact/', Data)
    
    #Verificando código pra redirecionamento temporário.
    def test_PostResp(self):
        self.assertEqual(302, self.response.status_code)

    #Conferindo se o email é gerado.
    def test_EmailForSending(self):
        self.assertEqual(1, len(mail.outbox))

#Testes para a mensagem de sucesso.
class SuccessMessage(TestCase):
    def test_SuccessMessage(self):
        #Dados para a simulação do envio.
        Data = dict(
                    name = "Vincent Moreira",
                    phone = "53-91234-5678",
                    email = "HeyViincy@gmail.com",
                    message = "Mensagem de contato"
                    )
        Response = self.client.post('/contact/', Data, follow=True)
        self.assertContains(Response, 'Sua mensagem foi enviada! Responderemos em breve!')