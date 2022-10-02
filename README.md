**Create a Login form with FlaskForm**

*The end result : [https://github.com/CiscoRostam/login-with-Flask.git](https://github.com/CiscoRostam/login-with-Flask)


References:
   * [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.0.x/)
   
   * [https://jinja.palletsprojects.com/en/3.1.x/templates/#import-context-behavior](https://jinja.palletsprojects.com/en/3.1.x/templates/#import-context-behavior)

   **Learning objectives:**

  * Create a web application with login form using:
    * Flask 
    * FlaskForm class(with validators)
    * Template Inheritance with Jinja2 
    * flask_bootstrap


**Challenge 1: Create a route “/login” that when the user clicks on “Login” will open the ‘login.html’**

   * Create an app decorator route with “/login”

   * Create a login function that render the “login.html” template. 

   * Add an [url_for()](https://tedboy.github.io/flask/generated/flask.url_for.html) mapped to ‘login’ function in the anchor <a> tag, like this when the user clicks on Login  
      button the user will be redirect to ‘login.html’

   - Refresh the browser and click on the Login button.     



**Challenge 2:  In main.py create a Form with WTForm([FlaskForm](https://flask-wtf.readthedocs.io/en/0.15.x/form/))**


* Install flask_wtf and wtforms:
   
   ```
      from flask_wtf import FlaskForm
      from wtforms import StringField,SubmitField```


* Create a class object call LoginForm that inherits from class FlaskForm and define the fields in the form with 
  wtforms class variables :
  
   
    ```
       class LoginForm(FlaskForm):
         email = StringField(label='email')
         password = StringField(label='password')
         submit = SubmitField(label='Log')```
	

**By default, WTForm  protects all forms against [Cross-Site Request Forgery (CSRF)](https://flask-wtf.readthedocs.io/en/1.0.x/csrf/#html-forms) attacks. To implement CSRF protection.**
	 

    `app = Flask(__name__)
     app.config['SECRET_KEY'] = 'Very secret string'`


**Challenge 3:  Render  the LoginForm on login.html template**

  * Create an object of LoginForm to pass as an argument in render_template() with a key/value pair.
      
      ```
         @app.route("/login")
         def login():
           form = LoginForm()

           return render_template('login.html',form=form)```

  * Render form in login.html
    
          ```<form >
          {{ form.csrf_token }}
          {{ form.email.label}}<br>{{ form.email(size=20) }}<br>
          {{ form.password.label }}<br>{{ form.password(size=20) }}<br>
          {{ form.submit }}
          </form>``` 


**HTTP Methods: To establish communication between the user and the servers, Flask routing decorator uses 
methods=[‘GET’,’POST’]. GET methods are by default in @app.route(). For security reasons we do POST requests when the
user  provides information to the server.**


**Challenge 4:  Add method POST**

  * Add method POST to @app.route(‘/login’)
       

     ```
        @app.route("/login", methods=['GET','POST'])
        def login():`

  * Add method POST to form tag in login.html file
      ```<form method="post">```

   - RUN the code to verify that user entered data is not in the browser


**The Form is working but is not completely functional, the form still doesn't know if  the email input is really an
email (text contains @), the user password is visible in the entry field, the data in both fields are not required and
there is no minimum and maximum amount of characters for the password.**


**Challenge 5: Instruct the form with validators argument**

   * Replace the [fields with the object class variables associated with the field](https://wtforms.readthedocs.io/en/2.3.x/fields/#wtforms.fields.StringField).
      
    
    ```from wtforms import SubmitField, PasswordField,EmailField```

   * Install [wtforms.validators](https://flask-wtf.readthedocs.io/en/1.0.x/quickstart/#validating-forms) and give it an optional validator to ensure that the field is not submitted empty 
      and a length for the password.
   `from wtforms.validators import DataRequired, Length`

   * Make the necessary changes in LoginForm class
    

    ` class LoginForm(FlaskForm):
         email = EmailField(label='email', validators=[DataRequired()])
         password = PasswordField(label='password',
                                 validators=[DataRequired(),
                                 Length(min=8, max=20)])
         submit = SubmitField(label='Log')`


  - RUN the code to verify if the data entries are valid.

**Challenge 6: Print user email in the console.**

  * Establish a condition in the login function that if the data from the form  is [validate_on_submit()](https://flask-wtf.readthedocs.io/en/0.15.x/quickstart/).printed
    the user email in the console. 

      
     ```
        @app.route("/login", methods=['GET','POST'])
        def login():
            form = LoginForm()
            if form.validate_on_submit():
                 print(form.email.data)

            return render_template('login.html',form=form)```

  * Add to  `<form>` the data from must be given action with an endpoint to redirect the data to the login function using Jinja2 {{ url_for() }}
    
    ` <form method="post" action="{{url_for('login')}}">`

   - RUN the code to verify if the user email is printed in the console.


**Now that we know that the LoginForm is receiving the data**


**Challenge 7: If user enter the predetermined email and password open “success.html”, else to “denied.html”**

   * If email: “admin@test.com” and password:”12345678”. Render 'success.html'.

   * Otherwise, render “denied.html” 

    `@app.route("/login", methods=['GET','POST'])
     def login():
            form = LoginForm()
            if form.validate_on_submit():
                if form.email.data == 'admin@email.com' 
                                       and form.password.data == '123':                
                return render_template('success.html')
                else:
                      return render_template('denied.html')
            return render_template('login.html',form=form)`

  
   - RUN the code to verify if the right email and password open 'success.html' and e if the user entries are different 
   from the predetermined condition  in the login function the 'denied.html' opens.

**Now the form is functional but will be nice to some styles on index.html and login.html  by using Bootstrap 
(Bootstrap is a web GUI framework. When Flask_bootstrap is initialised, a base template that includes all the Bootstrap
files are available in the app. This template takes advantage of Jinja2 template inheritance).**

First we have to look at [Template Inheritance with Jinja2](https://flask.palletsprojects.com/en/2.2.x/patterns/templateinheritance/)

        `<!DOCTYPE html>
        <html lang="en">
        <head>
           <meta charset="UTF-8">
           <title>{% block title%}{% endblock %}</title>
        </head>
        <body>
               {% block content%}{% endblock %}
        </body>
        </html>`


**Challenge 8: Extends ‘base.html’ to ‘index.html’ and ‘login.html’**

    `{% extends "base.html" %} `

   * Replace in ‘index.html’ and ‘login.html’ the <title> and <body> tag for {% block … %} and {% endblock%} .

   - RUN the app to notice that there is no change on the website.


**Challenge 9: Render the app with Bootstrap**

 **Follow  [Flask-Bootstrap documentation  instructions](https://pythonhosted.org/Flask-Bootstrap/basic-usage.html#):** 

   * Install flask_bootstrap extension and import Bootstrap.
 
   * Initialise Bootstrap in the app : Bootstrap(app)

   * Extend bootstrap to index.html and login.html

   - Refresh the app in the browser and see the change on the presentation.

**Now, everything looks good but still one extra thing to take total advantage of Flask_Bootstrap in this app.**

_**For next time  rather than type the whole code in <form> tag, there is a [WTForms support in Flask_Bootstrap](https://pythonhosted.org/Flask-Bootstrap/forms.html) that just
with one line of code the LoginForm is rendered in the login.html template.**_

   **Challenge 10: Uncomment all the code inside `<form> </form>` and replaced the form with ‘wtf.quick_form’**

   * Import the bootstrap/wtf.html at the top of login.html
        `{% import "bootstrap/wtf.html" as wtf %}`

   * Below to uncomment `<form></form>` tag. Type: `{{ wtf.quick_form(form) }}`

   - Refresh the browser and see the result.
