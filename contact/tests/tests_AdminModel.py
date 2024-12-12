from django.test import TestCase
from contact.models import Contact
from django.contrib.admin.sites import site

#Testes para o admin
class ContactAdmin(TestCase):
    #Verifica registro
    def test_ContactRegister(self):
        self.assertIn(Contact, site._registry)