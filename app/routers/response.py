from flask import Blueprint, request, jsonify
from app.models import db, Response, Question
from app.schemas.response import ResponseCreate, ResponseModel
from pydantic import ValidationError

response_bp = Blueprint('response', __name__, url_prefix='/responses')


@response_bp.route('/', methods=['GET'])
def get_responses():
    responses = Response.query.all()
    results = [ResponseModel.from_orm(response).dict() for response in responses]
    return jsonify(results), 200


@response_bp.route('/', methods=['POST'])
def add_response():
    try:
        data = ResponseCreate(**request.get_json())
    except ValidationError as e:
        return jsonify(e.errors()), 400

    question = Question.query.get(data.question_id)
    if not question:
        return jsonify({"message": "Question not found"}), 404

    response = Response(question_id=question.id, is_agree=data.is_agree)
    db.session.add(response)
    db.session.commit()

    return jsonify(ResponseModel.from_orm(response).dict()), 201
