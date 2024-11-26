from django.test import TestCase
from django.core import mail

#Testes para conferir a estrutura do Email.
class ContactPostValid(TestCase):
    def setUp(self):
        #Dados para a simulação do envio.
        Data = dict(
            name = "Vincent Moreira",
            phone = "53-91234-5678",
            email = "HeyViincy@gmail.com",
            message = "Mensagem de contato"
            )
        self.client.post('/contact/', Data)
        self.email = mail.outbox[0]

    #Assunto
    def test_Subject(self):
        Subject = "Contato Recebido"
        self.assertEqual(Subject, self.email.subject)
    
    #Remetente
    def test_From(self):
        From = "HeyViincy@gmail.com"
        self.assertEqual(From, self.email.from_email)

    #Destino
    def test_To(self):
        To = ["HeyViincy@gmail.com", "contato@eventif.com.br"]
        self.assertEqual(To, self.email.to)

    #Conferindo se os dados enviados constam no email.
    def test_EmailBody(self):
        #Dados
        Data = [
            "Vincent Moreira",
            "53-91234-5678",
            "HeyViincy@gmail.com",
            "Mensagem de contato"
            ]
        for String in Data:
            with self.subTest():
                self.assertIn(String, self.email.body)