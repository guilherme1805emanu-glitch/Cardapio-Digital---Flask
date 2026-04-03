from flask import Flask,render_template
from routes.auth import auth_routes
from flask_login import LoginManager
from definitions.dashboard import dashboard_routes  
from connection import db

from routes.inicio import app_inicio
from routes.categorias import categories_routes


app= Flask(__name__)
app.config['SECRET_KEY'] = 'qualquer-coisa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



app.config['SESSION_COOKIE_SECURE'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'


app.register_blueprint(app_inicio)
app.register_blueprint(categories_routes)

@app.route('/pizzas')
def route2():
    return render_template("pizzas.html")


@app.route('/promocoes')
def route3():
    return render_template("promoçoes.html")


@app.route('/bebidas')
def route4():
    return render_template("bebidas.html")


@app.route('/pontuação')
def route5():
    return render_template("pontuaçao.html")


@app.route("/pizzas-tradicionais")
def route6():
    return render_template("/pizzasTradicionais.html")


@app.route("/pizzas-artesanais")
def route7():
    return render_template("/pizzasartesanais.html")


@login_manager.user_loader
def load_user(user_id):
    from definitions.user import User
    return User.query.get(int(user_id))

app.register_blueprint(auth_routes, url_prefix='/auth')
app.register_blueprint(dashboard_routes)

with app.app_context():
    db.create_all()

app.run(debug=True)
