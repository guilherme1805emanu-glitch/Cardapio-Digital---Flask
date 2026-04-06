import enum
from sqlalchemy import Enum
from app.extensions import db


class CategoryType(enum.Enum):
    PIZZAS = "Pizzas"
    BEBIDAS = "Bebidas"


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    category_type = db.Column(
        Enum(CategoryType, name="category_type_enum", create_constraint=True),
        nullable=False
    )

    def __repr__(self):
        return f"<Category {self.name} - {self.category_type.value if self.category_type else 'N/A'}>"
