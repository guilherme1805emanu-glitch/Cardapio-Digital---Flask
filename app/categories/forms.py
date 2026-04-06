from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, ValidationError
from wtforms.validators import DataRequired, Length
from .models import Category, CategoryType


class CategoryForm(FlaskForm):
    name = StringField(
        "Nome da Category",
        validators=[
            DataRequired(message="O nome da categoria e obrigatorio"),
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
            raise ValidationError("Essa categoria ja existe.")

        field.data = nome
