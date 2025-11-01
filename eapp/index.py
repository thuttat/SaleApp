from flask import render_template

from eapp import app,dao


@app.route('/')
def index():
    categories = dao.load_categories()
    products = dao.load_products()
    return render_template('index.html', categories=categories,product=products)


if __name__ == "__main__":
    app.run(debug=True)
