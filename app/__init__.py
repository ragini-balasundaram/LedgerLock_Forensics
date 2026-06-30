from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required

# 1. Instantiate the database and login manager globally
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    # 2. Initialize the Flask application instance
    app = Flask(__name__)
    
    # 3. Configure application security and paths
    app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dfir.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 4. Link the extensions to this specific app instance
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login' # Kicks unauthenticated users to the login screen

    # 5. Define the user loader for Flask-Login session management
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))

    # 6. Register all modular Blueprints from the app/routes/ directory
    from app.routes.auth import auth_bp
    from app.routes.cases import cases_bp
    from app.routes.evidence import evidence_bp
    from app.routes.reports import reports_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(cases_bp)
    app.register_blueprint(evidence_bp)
    app.register_blueprint(reports_bp)

    # 7. The Main Live Dashboard Core Route
    @app.route('/')
    @login_required 
    def index():
        from app.models import Case, Evidence, ChainOfCustody
        
        # Query real database records for live metrics
        open_cases_count = Case.query.filter_by(status='Open').count()
        total_evidence_count = Evidence.query.count()
        pending_transfers_count = ChainOfCustody.query.filter(ChainOfCustody.purpose.contains('Pending')).count()
        
        # Fetch the 5 most recent entries to keep the activity feed current
        recent_activity = ChainOfCustody.query.order_by(ChainOfCustody.transfer_date.desc()).limit(5).all()
        
        return render_template(
            'index.html', 
            open_cases=open_cases_count, 
            total_evidence=total_evidence_count,
            pending_transfers=pending_transfers_count,
            recent_activity=recent_activity
        )

    return app