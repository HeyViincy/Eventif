# Generated by Django 5.1 on 2024-12-14 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_remove_contact_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='response',
            field=models.TextField(blank=True, max_length=200, verbose_name='Resposta'),
        ),
    ]
