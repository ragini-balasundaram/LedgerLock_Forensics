from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app import db
from app.models import Evidence

evidence_bp = Blueprint('evidence', __name__)
@evidence_bp.route('/evidence/log', methods=['GET', 'POST'])
@login_required
def log_evidence():
    if request.method == 'POST':
        # Logic to save to database
        new_evidence = Evidence(
            case_id=request.form.get('case_id'),
            evidence_tag=request.form.get('evidence_tag'),
            evidence_type=request.form.get('evidence_type'),
            hash_sha256="manual-entry-placeholder",
            collected_by=1
        )
        db.session.add(new_evidence)
        db.session.commit()
        return redirect(url_for('evidence.log_evidence'))
@evidence_bp.route('/search')
@login_required
def search():
    query = request.args.get('q') # Gets the text from the search bar
    # Find evidence where the tag matches the search query
    results = Evidence.query.filter(Evidence.evidence_tag.contains(query)).all()
    return render_template('search_results.html', results=results, query=query)
        
    return render_template('evidence.html')



