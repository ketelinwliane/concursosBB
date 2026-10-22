from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    name = StringField('Nome completo', validators=[
        DataRequired(message="O nome completo é obrigatório."),
        Length(min=2, max=150, message="O nome deve ter entre 2 e 150 caracteres.")
    ])
    email = StringField('E-mail', validators=[
        DataRequired(message="O e-mail é obrigatório."),
        Email(message="Informe um endereço de e-mail válido."),
        Length(max=255)
    ])
    submit = SubmitField('Inscrever-se')