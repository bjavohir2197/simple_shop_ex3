from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'

db = SQLAlchemy(app)


class Product():
    __tablename__ = 'Proudcts'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(150), nullable=True)
    price = db.Column(db.Float, nullable=True)
    description = db.Column(db.Text, nullable=True)
    image = db.Column(db.Text, nullable=True)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/add_product')
def add_product():
    return render_template('add_product.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/product_detail')
def product_detail():
    return render_template('product_detail.html')


@app.route('/products')
def products():
    return render_template('products.html')






if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)