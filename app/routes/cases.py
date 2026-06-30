from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app import db
from app.models import Case

cases_bp = Blueprint('cases', __name__)

@cases_bp.route('/cases')
@login_required
def list_cases():
    cases = Case.query.all()
    return render_template('cases/list.html', cases=cases)

@cases_bp.route('/case/new', methods=['GET', 'POST'])
@login_required
def new_case():
    if request.method == 'POST':
        # Simple extraction for now
        new_case = Case(
            case_number=request.form.get('case_number'),
            title=request.form.get('title'),
            lead_investigator_id=1 # Simplified: logic for current user would go here
        )
        db.session.add(new_case)
        db.session.commit()
        return redirect(url_for('cases.list_cases'))
    return render_template('cases/new_case.html')