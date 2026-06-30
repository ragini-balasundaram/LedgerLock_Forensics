from app import db
from datetime import datetime
from flask_login import UserMixin

class Role(db.Model):
    __tablename__ = 'roles'
    
    role_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(50), nullable=False, unique=True)
    
    # Relationship to User
    users = db.relationship('User', backref='role', lazy=True)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships to track what this user has done
    cases_led = db.relationship('Case', backref='lead_investigator', lazy=True)
    evidence_collected = db.relationship('Evidence', backref='collector', lazy=True)

    # Required by Flask-Login to manage sessions based on our custom primary key
    def get_id(self):
        return str(self.user_id)

class Case(db.Model):
    __tablename__ = 'cases'
    
    case_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    case_number = db.Column(db.String(30), nullable=False, unique=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='Open')
    lead_investigator_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    opened_date = db.Column(db.Date, default=datetime.utcnow)
    closed_date = db.Column(db.Date)
    
    # Cascade delete means if a case is deleted, its evidence is deleted too
    evidence_items = db.relationship('Evidence', backref='case', lazy=True, cascade="all, delete-orphan")

class Evidence(db.Model):
    __tablename__ = 'evidence'
    
    evidence_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    case_id = db.Column(db.Integer, db.ForeignKey('cases.case_id'), nullable=False)
    evidence_tag = db.Column(db.String(30), nullable=False, unique=True)
    description = db.Column(db.Text)
    evidence_type = db.Column(db.String(50), nullable=False)
    file_path = db.Column(db.String(255))
    hash_sha256 = db.Column(db.String(64), nullable=False)
    collected_by = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    collected_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='In Storage')
    
    chain_of_custody = db.relationship('ChainOfCustody', backref='evidence', lazy=True, cascade="all, delete-orphan")

class ChainOfCustody(db.Model):
    __tablename__ = 'chain_of_custody'
    
    custody_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    evidence_id = db.Column(db.Integer, db.ForeignKey('evidence.evidence_id'), nullable=False)
    from_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    to_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    transfer_date = db.Column(db.DateTime, default=datetime.utcnow)
    purpose = db.Column(db.String(150), nullable=False)
    
    # Specify foreign keys explicitly because two relationships point to the User table
    from_user = db.relationship('User', foreign_keys=[from_user_id], backref='transfers_given')
    to_user = db.relationship('User', foreign_keys=[to_user_id], backref='transfers_received')

class AuditLog(db.Model):
    __tablename__ = 'audit_log'
    
    log_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    action = db.Column(db.String(50), nullable=False) # e.g., 'CREATE', 'UPDATE', 'DELETE'
    target_table = db.Column(db.String(50), nullable=False)
    target_id = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    ip_address = db.Column(db.String(45))
    
    user = db.relationship('User', foreign_keys=[user_id])