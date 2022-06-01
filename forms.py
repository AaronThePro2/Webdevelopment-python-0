from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class PurchaseForm(FlaskForm):
    book1 = BooleanField('Book 1')
    book2 = BooleanField('Book 2')
    book3 = BooleanField('Book 3')
    book4 = BooleanField('Book 4')
    book5 = BooleanField('Book 5')
    firstname = StringField('Firstname', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    street = StringField('Street', validators=[DataRequired()])
    housenumber = StringField('Housenumber', validators=[DataRequired()])
    postcode = StringField('Post code', validators=[DataRequired()])
    livingarea = StringField('Livingarea', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    phonenumber = StringField('Phonenumber')
    email = StringField('Email', validators=[DataRequired()])
    delivery = BooleanField('Delivery')
    submit = SubmitField('Verstuur order')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')