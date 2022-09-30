from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, EmailField,PasswordField
from wtforms.validators import DataRequired, Length
class LoginForm(FlaskForm):
    email = EmailField(label='email',validators=[DataRequired()])
    password = PasswordField(label='password',validators=[DataRequired(),Length(min=4,max=10,message='min 4 and max 10'
                                                                                                     'characters, please')])
    submit = SubmitField(label='Log')

app = Flask(__name__)
app.config['SECRET_KEY']='seCRET_KEY_VERY_SECURE'
@app.route("/")
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    print(form.email.data)
    return render_template('login.html', form=form)




if __name__ == '__main__':
    app.run(debug=True)