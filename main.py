from flask import Flask,render_template
from routes.auth import auth_routes
from flask_login import LoginManager
from definitions.dashboard import dashboard_routes  
from connection import db

from routes.welcome import app_welcome
from routes.home import app_home
from routes.categories import categories_routes


app= Flask(__name__)
app.config['SECRET_KEY'] = 'qualquer-coisa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



app.config['SESSION_COOKIE_SECURE'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'


app.register_blueprint(app_welcome)
app.register_blueprint(app_home)
app.register_blueprint(categories_routes)

@app.route('/pizzas')
def route_pizzas():
    return render_template("pizzas.html")


@app.route('/promotion')
def route_promotion():
    return render_template("promotion.html")


@app.route('/drinks')
def route_drinks():
    return render_template("drinks.html")


@app.route('/score')
def route_score():
    return render_template("score.html")


@app.route("/traditional-pizzas")
def route_tradicional_pizza():
    return render_template("/traditionalPizzas.html")


@app.route("/artisan-pizzas")
def route_artisan_pizzas():
    return render_template("/artisanPizzas.html")


@login_manager.user_loader
def load_user(user_id):
    from definitions.user import User
    return User.query.get(int(user_id))

app.register_blueprint(auth_routes, url_prefix='/auth')
app.register_blueprint(dashboard_routes)

with app.app_context():
    db.create_all()

app.run(debug=True)
