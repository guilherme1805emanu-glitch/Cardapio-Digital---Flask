from connection import db
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, ValidationError
from wtforms.validators import DataRequired, Length
import enum
from sqlalchemy import Enum


class CategoryType(enum.Enum):
    PIZZAS = "Pizzas"
    BEBIDAS = "Bebidas"


class CategoryForm(FlaskForm):
    name = StringField(
        "Nome da Category",
        validators=[
            DataRequired(message="O nome da categoria é obrigatório"),
            Length(min=2, max=50, message="O nome da categoria deve ter entre 2 e 50 caracteres")
        ]
    )

    category_type = SelectField(
        "Tipo da Category",
        choices=[(tag.name, tag.value) for tag in CategoryType],
        coerce=lambda x: CategoryType[x],
        validators=[DataRequired()]
    )

    def validate_name(self, field):
        nome = field.data.strip().title()

        category = Category.query.filter_by(name=nome).first()
        if category:
            raise ValidationError("Essa categoria já existe.")

        field.data = nome

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique= True)
    category_type = db.Column(
        Enum(CategoryType, name="category_type_enum", create_constraint=True),
        nullable=False
    )
    def __repr__(self):
        return f"<Category {self.name} - {self.category_type.value if self.category_type else 'N/A'}>"