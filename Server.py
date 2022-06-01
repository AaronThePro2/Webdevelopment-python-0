import math
from copyreg import constructor
from operator import methodcaller
from subprocess import CREATE_NEW_CONSOLE
from flask import Flask, render_template, redirect
from forms import LoginForm, PurchaseForm
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = "A0Zr98j/3yXdfgR~sfsdfsdfXHH!jmN"

@app.route("/")
def index():
    return render_template(
        'index.html') 

@app.route("/shop/")
def user():
   return render_template(
      'shop.html', price1 = "24,24€", price2 = "12,10€", price3="19,08€", price4="33,08€", price5="45,56€")


@app.route('/base/')
def base():
    return render_template(
      'base.html')

@app.route('/contact/')
def contact():
    return render_template(
        'contact.html')


@app.route('/login/', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/shop/')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/purchase/', methods=["GET", "POST"])
def purchase():
    form = PurchaseForm()
    if form.validate_on_submit():
        totalprice = 0
        book1 = request.form.get('book1')
        book2 = request.form.get('book2')
        book3 = request.form.get('book3')
        book4 = request.form.get('book4')
        book5 = request.form.get('book5')
        if (book1 == "y"):
            totalprice += 24.24
        if (book2 == "y"):
            totalprice += 12.10
        if (book3 == "y"):
            totalprice += 19.08
        if (book4 == "y"):
            totalprice += 33.08
        if (book5 == "y"):
            totalprice += 45.56
        totalprice = "{:.2f}".format(totalprice)
        return render_template('bedankt.html', tprice = totalprice)
    return render_template('bestelpagina.html', title="Bestelpagina", form=form, price1 = "24,24€", price2 = "12,10€", price3="19,08€", price4="33,08€", price5="45,56€")


app.run(debug=True)