from flask import current_app, render_template, url_for
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
from app import mail
import logging

TOKEN_SALT = "registration-status-v1"
TOKEN_MAX_AGE_SECONDS = 60 * 60 * 24 * 30

def make_registration_token(registration_id):
    serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"], salt=TOKEN_SALT)
    return serializer.dumps({"registration_id": registration_id})

def read_registration_token(token):
    serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"], salt=TOKEN_SALT)
    return serializer.loads(token, max_age=TOKEN_MAX_AGE_SECONDS)

def send_registration_confirmation(recipient, name, registration_id):
    """Envia confirmação com link assinado para consultar o status da inscrição."""
    try:
        token = make_registration_token(registration_id)
        status_url = url_for("main.phishing_simulation", _external=True)
        msg = Message(
            subject="Confirmação de cadastro — projeto acadêmico (simulação)",
            recipients=[recipient],
        )
        msg.body = (
            f"Olá, {name}!\n\n"
            "Recebemos seu cadastro no projeto acadêmico de demonstração.\n"
            f"Acesse o link da atividade: {status_url}\n\n"
            "Este é um projeto educacional e não é um canal oficial do Banco do Brasil.\n"
            "Se você não realizou esse cadastro, pode ignorar esta mensagem."
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
