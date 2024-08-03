from flask import Blueprint, request
from app.models import db, Response

response_bp = Blueprint('response', __name__, url_prefix='/responses')


@response_bp.route('/', methods=['GET'])
def get_responses():
    responses = Response.query.all()
    return {"responses": [str(response) for response in responses]}


@response_bp.route('/', methods=['POST'])
def add_response():
    data = request.json
    new_response = Response(question_id=data['question_id'], is_agree=data['is_agree'])
    db.session.add(new_response)
    db.session.commit()
    return {"message": "Response added"}, 201
