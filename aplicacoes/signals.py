from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _

from aplicacoes.models import Edital, Email

@receiver(post_save, sender=Edital)
def enviar_email_novo_edital(sender, instance, created, **kwargs):
    if created:
        # Assunto do e-mail
        subject = _('Novo Edital Disponível')

        # Obtém todos os endereços de e-mail e nomes do modelo Email
        destinatarios = Email.objects.values_list('email', 'nome')

        # Pega o primeiro destinatário
        destinatario = destinatarios.first()

        # Constrói a lista de destinatários formatada como (nome, e-mail)
        to_email_list = ['{} <{}>'.format(nome, email) for email, nome in destinatarios]

        # Mensagem do e-mail em HTML com o campo nome disponível
        html_message = render_to_string('aplicacoes/emailEdital.html', {'edital': instance, 'destinatario': destinatario})

        # Mensagem do e-mail em texto sem formatação
        plain_message = strip_tags(html_message)

        # Remetente do e-mail (substitua pelo seu e-mail)
        from_email = 'luizeduardo00736@gmail.com'

        # Envie o e-mail para todos os destinatários
        send_mail(subject, plain_message, from_email, to_email_list, html_message=html_message)
