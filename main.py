from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('signup_template.html')
    return template.render()

 #Begin Validate User Signup block   

@app.route('/', methods=['POST'])
def validate_user():
   username=request.form['username']
   password=request.form['password']
   v_password=request.form['verify']
   user_email=request.form['email']

   username_error= ''
   password_error= ''
   v_error=''
   email_error=''

   space = ' '
   blank = ''
   min_len=3
   max_len=20

   #check if Username, PW, or Verify PW have been left blank
   if (username==''):
       username_error = "Dont leave blank"
   if (password==''):
       password_error = "Dont leave blank" 
   if (v_password==''):
       v_error = "Dont leave blank" 

   #check if passwords match
   if (password!=v_password):
      password_error = "Passwords do not match"
      v_verify="Passwords do not match"

    #TO DO Verify Password Characters
   if (username!=blank):
      if space in username:
         username_error="I said no spaces!"
      if ((len(username)<min_len) | (len(username)>max_len)):
         username_error= "Please use a User Name between 3 and 20 characters"


    #To DO Verify Email Characters
   if (user_email!=blank):
      if space in user_email:
         email_error="I said no spaces!"
      if '@' not in user_email:
         email_error = "Valid emails have an @ symbol"
      if '.' not in user_email:
         email_error= "Valid emails have a . in them"
      if (len(user_email)<min_len) | (len(user_email)>max_len):
         email_error= "Please use a User Name between 3 and 20 characters"



   #Place holder code if User gets all requirements right ... it will do something else later
   if((username_error==blank) and (password_error==blank) and (v_error==blank) and (email_error==blank)):
      username_error= 'SUCCESS!'
      password_error= 'SUCCESS!'
      v_error='SUCCESS!'
      email_error='SUCCESS!'

   template = jinja_env.get_template('signup_template.html')

   return template.render(username_error=username_error,
      password_error=password_error,
      verify_error=password_error,
      email_error=email_error)

# End User Validation Procedure


app.run()
