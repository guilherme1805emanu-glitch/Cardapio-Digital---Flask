from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField
from wtforms.validators import DataRequired, Length, Email, Regexp


class LoginForm(FlaskForm):
    email = EmailField(
        "Email",
        validators=[
            DataRequired(message="O Email e obrigatorio"),
            Email(message="O Email deve ser valido")
        ]
    )
    password = PasswordField(
        "Senha",
        validators=[DataRequired(message="A senha e obrigatoria")]
    )


class RegisterForm(FlaskForm):
    username = StringField(
        'Nome de usuario',
        validators=[
            DataRequired(message="O nome e obrigatorio"),
            Length(min=3, max=20, message="O nome deve ter entre 3 e 20 caracteres")
        ]
    )
    email = StringField(
        'Email',
        validators=[
            DataRequired(message="O email e obrigatorio"),
            Email(message="Email invalido")
        ]
    )
    password = PasswordField(
        'Senha',
        validators=[
            DataRequired(message="A senha e obrigatoria"),
            Length(min=6, message="A senha deve ter no minimo 6 caracteres")
        ]
    )
    telephone = StringField(
        'Telefone',
        validators=[
            DataRequired(message="O telefone e obrigatorio"),
            Regexp(r'^\d{10,11}$', message="Digite um telefone valido (somente numeros)")
        ]
    )
    address = StringField(
        'Endereco',
        validators=[
            DataRequired(message="O endereco e obrigatorio"),
            Length(min=5, message="Endereco muito curto")
        ]
    )
