from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField
from wtforms.validators import DataRequired, Length, Email, Regexp
from werkzeug.security import generate_password_hash, check_password_hash 
from connection import db

class RegisterForm(FlaskForm):
    username = StringField(
        'Nome de usuário',
        validators=[
            DataRequired(message="O nome é obrigatório"),
            Length(min=3, max=20, message="O nome deve ter entre 3 e 20 caracteres")
        ]
    )

    email = StringField(
        'Email',
        validators=[
            DataRequired(message="O email é obrigatório"),
            Email(message="Email inválido")
        ]
    )

    password = PasswordField(
        'Senha',
        validators=[
            DataRequired(message="A senha é obrigatória"),
            Length(min=6, message="A senha deve ter no mínimo 6 caracteres")
        ]
    )

    telephone = StringField(
        'Telefone',
        validators=[
            DataRequired(message="O telefone é obrigatório"),
            Regexp(r'^\d{10,11}$', message="Digite um telefone válido (somente números)")
        ]
    )

    address = StringField(
        'Endereço',
        validators=[
            DataRequired(message="O endereço é obrigatório"),
            Length(min=5, message="Endereço muito curto")
        ]
    )
class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(message= "O Email é obrigatório"), Email(message="O Email deve ser válido")])
    password = PasswordField("Senha", validators=[DataRequired(message="A senha é obrigatória")])

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password_hash = db.Column(db.String(256))
    username = db.Column(db.String(50))
    phone = db.Column(db.String(15))
    address = db.Column(db.String(100))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)