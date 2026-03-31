from connection import db
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired,Length

class PizzaDoceForm(FlaskForm):
    name = StringField("Nome da Pizza Doce", 
                       validators=[DataRequired(message="O nome da Pizza doce é obrigatório"), 
                                    Length(min=2, max=50, message="O nome da Pizza doce deve ter entre 2 e 50 caracteres")])
    

class PizzaDoce(db.Model):
    __tablename__ = 'pizzas_doces'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    image_url = db.Column(db.String(200), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    category = db.relationship('Categoria', backref=db.backref('pizzas_doces', lazy=True))


