from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required
from app.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # 1. Look up the user in the database by email
        user = User.query.filter_by(email=email).first()
        
        # 2. If user exists AND the password hash matches
        if user and check_password_hash(user.password_hash, password):
            # 3. Log them in and create a session cookie!
            login_user(user)
            print("LOGIN SUCCESSFUL!")
            return redirect(url_for('index')) # Send them to the homepage for now
            
        else:
            print("LOGIN FAILED: Invalid credentials")
            # We will add a UI error message here later
            return redirect(url_for('auth.login'))

    return render_template('login.html')