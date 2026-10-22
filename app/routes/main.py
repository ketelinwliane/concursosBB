from flask import Blueprint, jsonify, render_template
from app.forms.registration import RegistrationForm
from app.routes.menu import EXTERNAL_ROUTES

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    form = RegistrationForm()
    return render_template('index.html', form=form, external_routes=EXTERNAL_ROUTES)


@main_bp.route('/inscricao/sucesso')
def success():
    return render_template('success.html', external_routes=EXTERNAL_ROUTES)


@main_bp.route('/health')
def health():
    return jsonify({'status': 'ok'}), 200


@main_bp.route('/voce-caiu-no-phishing')
def phishing_simulation():
    """Página de encerramento da simulação educativa de phishing."""
    return render_template('phishing_simulation.html', external_routes=EXTERNAL_ROUTES)


@main_bp.route('/seguranca-digital')
def phishing_awareness():
    """Página educativa sobre phishing usada no projeto acadêmico."""
    return render_template('phishing_awareness.html', external_routes=EXTERNAL_ROUTES)
