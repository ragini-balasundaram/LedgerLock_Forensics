from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app import db
from app.models import Evidence

evidence_bp = Blueprint('evidence', __name__)

@evidence_bp.route('/evidence/log', methods=['GET', 'POST'])
@login_required
def log_evidence():
    if request.method == 'POST':
        # Logic to save to DB will go here once you finalize the form!
        return redirect(url_for('index'))
        
    return render_template('evidence.html')