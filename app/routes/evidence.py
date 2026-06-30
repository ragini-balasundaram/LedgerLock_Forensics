from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app import db
from app.models import Evidence, Case, ChainOfCustody
import uuid # Used to generate a fake secure hash for the prototype

evidence_bp = Blueprint('evidence', __name__)

@evidence_bp.route('/evidence/log', methods=['GET', 'POST'])
@login_required
def log_evidence():
    if request.method == 'POST':
        # 1. Create the Evidence Record
        new_evidence = Evidence(
            case_id=request.form.get('case_id'),
            evidence_tag=request.form.get('evidence_tag'),
            evidence_type=request.form.get('evidence_type'),
            hash_sha256=request.form.get('hash_sha256'),
            collected_by=current_user.user_id,
            status='In Storage'
        )
        db.session.add(new_evidence)
        db.session.flush() # This assigns an ID to new_evidence BEFORE we fully commit

        # 2. Create the Chain of Custody Log automatically!
        new_coc = ChainOfCustody(
            evidence_id=new_evidence.evidence_id,
            to_user_id=current_user.user_id,
            purpose='Logged Initial Evidence' # This text will show on your dashboard
        )
        db.session.add(new_coc)
        
        # 3. Save both to the database
        db.session.commit()
        return redirect(url_for('index')) # Kick back to dashboard to see the update
        
    # If GET request, fetch active cases to populate the dropdown
    active_cases = Case.query.filter_by(status='Open').all()
    
    # Generate a random dummy hash for the UI form
    dummy_hash = uuid.uuid4().hex + uuid.uuid4().hex 
    return render_template('evidence/log.html', cases=active_cases, dummy_hash=dummy_hash)