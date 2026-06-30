from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager # <-- ADD THIS
from flask import render_template
from flask_login import login_required


db = SQLAlchemy()
login_manager = LoginManager() # <-- ADD THIS

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dfir.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    # <-- ADD THESE 6 LINES -->
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login' # Where to send users if they aren't logged in

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))

    @app.route('/')
    @login_required 
    def index():
        return render_template('index.html')

    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)
    
    from app.routes.evidence import evidence_bp
    app.register_blueprint(evidence_bp)

    return app