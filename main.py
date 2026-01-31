from flask import Flask,render_template

app= Flask(__name__)

@app.route('/')
def route1():
    return render_template("inicio.html")

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


@app.route("/pizzas_tradicionais")
def route6():
    return render_template("/pizzasTradicionais.html")


@app.route("/pizzas_artesanais")
def route7():
    return render_template("/pizzasartesanais.html")

app.run(debug=True)
