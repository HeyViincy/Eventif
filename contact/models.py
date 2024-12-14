from django.db import models


class Contact(models.Model):
    name = models.CharField('Nome', max_length=100)
    phone = models.CharField('Telefone', max_length=20, blank=True)
    email = models.EmailField('E-Mail')
    message = models.TextField('Mensagem', max_length=200)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    response = models.TextField('Resposta', max_length=200, blank=True)
    response_sent_at = models.DateTimeField('Respondido em', null=True, blank=True)
    flag = models.BooleanField('Já foi respondido', default=False)

    class Meta:
        verbose_name_plural = 'contatos'
        verbose_name = 'contato'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name