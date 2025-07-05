from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
from datetime import datetime, timedelta
import random, os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['MAIL_SERVER'] = 'smtp.example.com'  # <-- Replace with your SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your_email@example.com'  # <-- Replace with your email
app.config['MAIL_PASSWORD'] = 'your_email_password'      # <-- Replace with your email password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
mail = Mail(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    otp = db.Column(db.String(6))
    otp_expiry = db.Column(db.DateTime)

@app.route('/')
def home():
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('register'))
        if User.query.filter_by(email=email).first():
            flash('Email already exists')
            return redirect(url_for('register'))
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            otp = str(random.randint(100000, 999999))
            user.otp = otp
            user.otp_expiry = datetime.utcnow() + timedelta(minutes=5)
            db.session.commit()
            # Send OTP via email
            try:
                msg = Message('Your OTP Code', sender=app.config['MAIL_USERNAME'], recipients=[user.email])
                msg.body = f'Your OTP code is {otp}. It expires in 5 minutes.'
                mail.send(msg)
            except Exception as e:
                flash('Failed to send OTP email. Please check your mail configuration.')
                return redirect(url_for('login'))
            session['user_id'] = user.id
            flash('OTP sent to your email.')
            return redirect(url_for('verify_otp'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    user = User.query.get(session.get('user_id'))
    if not user:
        return redirect(url_for('login'))
    if request.method == 'POST':
        otp = request.form['otp']
        if user.otp == otp and user.otp_expiry and user.otp_expiry > datetime.utcnow():
            user.otp = None
            user.otp_expiry = None
            db.session.commit()
            session['authenticated'] = True
            return redirect(url_for('success'))
        flash('Invalid or expired OTP')
    return render_template('verify_otp.html')

@app.route('/success')
def success():
    if not session.get('authenticated'):
        return redirect(url_for('login'))
    return render_template('success.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)