from flask import Blueprint, request, jsonify, current_app

job_bp = Blueprint('job_bp', __name__)

@job_bp.route('/jobs/data', methods=['GET'])
def get_jobs():
    search_term = request.args.get('searchTerm', '')
    page = int(request.args.get('page', 1))
    rows_per_page = int(request.args.get('rowsPerPage', 10))
    offset = (page - 1) * rows_per_page

    job_model = current_app.config['JOB_MODEL']
    jobs = job_model.get_all_jobs(search_term, offset, rows_per_page)
    return jsonify(jobs)

@job_bp.route('/jobs/check-db-connection', methods=['GET'])
def check_db_connection():
    job_model = current_app.config['JOB_MODEL']
    return jsonify(success=job_model.check_connection())
