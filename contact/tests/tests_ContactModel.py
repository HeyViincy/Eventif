from django.test import TestCase
from datetime import datetime
from contact.models import Contact

#Testes sobre a estrutura do model
class ModelContact(TestCase):
    def setUp(self):
        self.obj = Contact(
            name = "Vincent Moreira",
            phone = "53-91234-5678",
            email = "HeyViincy@gmail.com",
            message = "Mensagem de contato"
        )
        self.obj.save()

    #Confere se o objeto é criado
    def test_Created(self):
        self.assertTrue(Contact.objects.exists())

    #Confere o campo created_at
    def test_CreatedAt(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    #Confere Str
    def test_Identificator(self):
        self.assertEqual('Vincent Moreira', str(self.obj))

    #Confere se o flag autommaticamente é false
    def test_FlagDefault(self):
        self.assertEqual(False, self.obj.flag)

    #Confere se o campo response_sent_at pode ser nulo
    def test_ResponseSentAt(self):
        field = Contact._meta.get_field('response_sent_at')
        self.assertTrue(field.null)