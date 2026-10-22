from flask import render_template, url_for
from flask_mail import Message
from app import mail
import logging


def send_registration_confirmation(recipient, name):
    """Envia confirmação sem armazenar o cadastro em banco de dados."""
    try:
        status_url = url_for("main.phishing_simulation", _external=True)
        msg = Message(
            subject="Confirmação de cadastro — projeto acadêmico (simulação)",
            recipients=[recipient],
        )
        msg.body = (
            f"Olá, {name}!\\n\\n"
            "Recebemos seus dados nesta demonstração acadêmica. "
            "Eles não foram armazenados em um banco de dados.\\n"
            f"Acesse o link da atividade: {status_url}\\n\\n"
            "Este é um projeto educacional e não é um canal oficial do Banco do Brasil."
        )
        msg.html = render_template(
            "email/registration_confirmation.html",
            name=name,
            status_url=status_url,
        )
        mail.send(msg)
        return True
    except Exception:
        logging.exception("Não foi possível enviar a confirmação de cadastro.")
        return False
