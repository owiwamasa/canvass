from flask import Blueprint, jsonify, request
from flask_login import current_user
from app.models import Job, User, db
from app.forms import CreateJobForm


job_routes = Blueprint('jobs', __name__)


@job_routes.route('/', methods=['POST'])
def create_job():
    form = CreateJobForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    print('-------------------------', form.data)
    if form.validate_on_submit():
        job = Job(
            title = form.title.data,
            description = form.description.data,
            dueDate = form.dueDate.data,
            userId = form.userId.data,
            artistId = form.artistId.data
        )
        db.session.add(job)
        db.session.commit()
        return job.toDict()
    errors = form.errors
    return jsonify([f'{field.capitalize()}: {error}'
                for field in errors
                for error in errors[field]]),400