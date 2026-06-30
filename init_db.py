from app import create_app, db
from app.models import User, Role
from werkzeug.security import generate_password_hash

# 1. Boot up the app context
app = create_app()

with app.app_context():
    # 2. This command actually reads models.py and builds the tables!
    db.create_all()
    print("Database tables created successfully!")

    # 3. Create the Admin Role
    admin_role = Role.query.filter_by(role_name='Admin').first()
    if not admin_role:
        admin_role = Role(role_name='Admin')
        db.session.add(admin_role)
        db.session.commit()

    # 4. Create the Master Admin User
    admin_user = User.query.filter_by(email='admin@ledgerlock.com').first()
    if not admin_user:
        hashed_pw = generate_password_hash('SecurePass123!')
        admin_user = User(
            username='admin_boss', 
            email='admin@ledgerlock.com', 
            password_hash=hashed_pw, 
            role_id=admin_role.role_id
        )
        db.session.add(admin_user)
        db.session.commit()
        print("Master Admin account injected successfully!")
    else:
        print("Admin account already exists.")