from flask import Flask,render_template

app= Flask(__name__)

@app.route('/')
def route1():
    return render_template("inicio.html")


@app.route('/Pizzas Tradicionáis')
def route2():
    return render_template("pizzasTradicionais.html")


@app.route('/Pizzas Artesanáis')
def route3():
    return render_template("pizzasArtesanais.html")


@app.route('/Pizzas Metade Metade')
def route4():
    return render_template("pizzasMetade.html")


@app.route('/Pizzas Promoções do Dia')
def route5():
    return render_template("promoçoes.html")


@app.route('/Bebidas')
def route6():
    return render_template("bebidas.html")


@app.route('/Pontuação')
def route7():
    return render_template("pontuaçao.html")


app.run(debug=True)
