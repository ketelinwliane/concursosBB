from flask import Blueprint, flash, redirect, url_for
from app.forms.registration import RegistrationForm
from app.services.email_service import send_registration_confirmation

registration_bp = Blueprint('registration', __name__)


@registration_bp.route('/inscricao', methods=['POST'])
def register():
    form = RegistrationForm()

    if not form.validate_on_submit():
        for errors in form.errors.values():
            for error in errors:
                flash(error, 'danger')
        return redirect(url_for('main.index') + '#inscricao')

    name = form.name.data.strip()
    email = form.email.data.strip().lower()

    # Sem banco de dados: os dados são usados apenas durante esta requisição.
    email_sent = send_registration_confirmation(email, name)
    if email_sent:
        return redirect(url_for('main.success'))

    flash('Não foi possível enviar a confirmação. Verifique a configuração de e-mail e tente novamente.', 'danger')
    return redirect(url_for('main.index') + '#inscricao')
