from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField

class LoginForm(FlaskForm):
    email = StringField(label='email')
    password = StringField(label='pasword')
    submit = SubmitField(label='Log')
app = Flask(__name__)
app.config['SECRET_KEY']='seCRET_KEY_VERY_SECURE'
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    form = LoginForm()

    return render_template('login.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)