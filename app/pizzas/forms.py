from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class PizzaDoceForm(FlaskForm):
    name = StringField(
        "Nome da Pizza Doce",
        validators=[
            DataRequired(message="O nome da Pizza doce e obrigatorio"),
            Length(min=2, max=50, message="O nome da Pizza doce deve ter entre 2 e 50 caracteres")
        ]
    )
