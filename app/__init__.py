from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the database globally so other files (like models) can access it
db = SQLAlchemy()

def create_app():
    # Initialize the Flask application
    app = Flask(__name__)
    
    # Configure the app (we will move these to a .env file later)
    app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dfir.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Bind the database to this app
    db.init_app(app)

    # A simple test route just to make sure it works before we build the UI
    @app.route('/')
    def index():
        return "<h2>LedgerLock Forensics Server is Running! 🔐</h2>"

    # (We will register our auth and case blueprints here in the next step)

    return app