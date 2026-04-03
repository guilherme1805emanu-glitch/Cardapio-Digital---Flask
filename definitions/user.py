from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField
from wtforms.validators import DataRequired, Length, Email, Regexp
from werkzeug.security import generate_password_hash, check_password_hash 
from connection import db

class RegisterForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(message= "O Email é obrigatório!"), Email(message="O Email deve ser válido!")])
    password = PasswordField("Senha", validators=[DataRequired(message= "A senha é obrigatória"), Length(min=6, message="A senha deve ter pelo menos 6 caracteres")])
    username = StringField("Nome", validators=[DataRequired(message= "O seu nome é obrigatório"), Length(min=2, max=50, message="O nome deve ter entre 2 e 50 caracteres")])
    telephone = StringField("Telefone", validators=[DataRequired(),Length(min=8, max=11), Regexp(r'^\d{10,15}$', message="O telefone deve conter apenas números e ter entre 10 e 15 dígitos.")])
    address = StringField("Endereço", validators=[DataRequired( message= "O Endereço é obrigatório"), Length(min=5, max=100, message="O endereço deve ter entre 5 e 100 caracteres")])

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