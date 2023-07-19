from flask import Flask, render_template, url_for, request, flash, redirect, session
from clients_sql import check_user, add_user, check_verification,verification_done
from admin_sql import is_admin,check_admin,create_admin_table
from functools import wraps
from flask_mail import *
from random import randint


app = Flask(__name__)
app.secret_key = 'upasana12345'


#configure flask mail

app.config['MAIL_SERVER']='smtp.gmail.com'  
app.config['MAIL_PORT']=465  
app.config['MAIL_USERNAME'] = 'sharmaupasana823@gmail.com'  
app.config['MAIL_PASSWORD'] = 'xkkzgbuvozqhrhmf'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  

mail = Mail(app)

#------------------------------------------------------------------
def login_required(func):
    @wraps(func)
    def secure_function(*args, **kwargs):
        if "email_client" not in session:
            return redirect(url_for("login", next=request.path))
        return func(*args, **kwargs)
    return secure_function
def admin_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if "email_admin" not in session:
            flash('You do not have access to this page.', category='error')
            return redirect(url_for('admin'))
        return func(*args, **kwargs)
    return decorated_function

#----------------------------------------------------------------------

@app.route('/')
def home():
    return render_template('home.html')


otp = randint(000000,999999)  
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        password = request.form.get('password')
        if len(password) < 8:
             flash('Password must be at least 7 characters.', category='error')
        else:
            add_user(firstname, lastname, email, password, verification=0)
            flash('Account created!', category='success')     
            return redirect(url_for('verify', email = email, password = password))        
    return render_template('register.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if check_user(email,password):
            if check_verification(email, password) == 0:
                return redirect(url_for('verify', email = email, password = password))
            session['email_client'] = request.form.get('email')
            return render_template('clients.html')
        else:
            flash('Invalid credentials', category='error')
    return render_template('login.html')


@app.route('/verify', methods=['POST','GET'])
def verify():
    email = request.args.get('email')
    password = request.args.get('password')
    if request.method == 'POST':
        user_otp = request.form.get('otp')
        if otp == int(user_otp):
            verification_done(email, password)
            return redirect(url_for('validate'))
        else:
            return render_template('verify.html', error='Invalid OTP')
    msg = Message('OTP', sender= 'no_reply@app.com', recipients=[email])
    msg.body = str(otp)
    mail.send(msg)      
    return render_template('verify.html')
    
@app.route('/validate', methods=['GET'])
def validate():
    return render_template('validate.html')

@app.route('/clients', methods=['GET', 'POST'])
@login_required
def clients():
    return render_template('clients.html')


@app.route('/logout')
def logout():
    session.pop('email_client', None)
    session.clear()
    return redirect(url_for('home'))

@app.route('/admin', methods=['POST', 'GET'])
def admin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if check_admin(email, password):
            session['email_admin'] = request.form.get('email')
            return redirect(url_for('admin_website'))
        else:
            return "SORRY YOU CANNOT ACCESS THE PAGE"
    return render_template('admin_login.html')
#-------------------------------------------------------
@app.before_request
def before_request():
    # Check if user session is still valid
    if 'email' in session and not is_user_valid(session['email']):
        session.clear()

def is_user_valid(email):
    # Implement your logic to check if the user is still valid
    # Return True if the user is valid, False otherwise
    return True
#-------------------------------------------------------------

@app.route('/adminwebsite') 
@admin_required
def admin_website():
    return render_template('admin_main.html')

@app.route('/logout')
def logout_admin():
    session.pop('email_admin', None)
    session.clear()
    return redirect(url_for('admin'))
    

if __name__=='__main__':
    app.run(debug=True)

