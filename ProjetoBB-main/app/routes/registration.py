from flask import Blueprint, flash, redirect, url_for
from app import db
from app.forms.registration import RegistrationForm
from app.models.registration import Registration
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

    if Registration.query.filter_by(email=email).first():
        flash('Este e-mail já está cadastrado em nossa base.', 'danger')
        return redirect(url_for('main.index') + '#inscricao')

    registration = Registration(name=name, email=email)

    try:
        db.session.add(registration)
        db.session.commit()
        send_registration_confirmation(email, name, registration.id)
        return redirect(url_for('main.success'))
    except Exception:
        db.session.rollback()
        flash('Ocorreu um erro interno ao processar sua inscrição. Tente novamente.', 'danger')
        return redirect(url_for('main.index') + '#inscricao')
