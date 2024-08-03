from flask import Blueprint, request, jsonify
from app.models import db, Question, Category
from app.schemas.question import QuestionCreate, QuestionResponse
from pydantic import ValidationError

questions_bp = Blueprint('questions', __name__, url_prefix='/questions')


@questions_bp.route('/', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    results = [QuestionResponse.from_orm(question).dict() for question in questions]
    return jsonify(results)


@questions_bp.route('/', methods=['POST'])
def create_question():
    try:
        data = QuestionCreate(**request.get_json())
    except ValidationError as e:
        return jsonify(e.errors()), 400

    category = Category.query.get(data.category_id)
    if not category:
        return jsonify({"message": "Category not found"}), 404

    question = Question(text=data.text, category_id=data.category_id)
    db.session.add(question)
    db.session.commit()

    return jsonify(QuestionResponse.from_orm(question).dict()), 201


@questions_bp.route('/<int:id>', methods=['GET'])
def get_question(id):
    question = Question.query.get_or_404(id)
    return jsonify(QuestionResponse.from_orm(question).dict())


@questions_bp.route('/<int:id>', methods=['PUT'])
def update_question(id):
    try:
        data = QuestionCreate(**request.get_json())
    except ValidationError as e:
        return jsonify(e.errors()), 400

    question = Question.query.get_or_404(id)

    category = Category.query.get(data.category_id)
    if not category:
        return jsonify({"message": "Category not found"}), 404

    question.text = data.text
    question.category_id = data.category_id
    db.session.commit()

    return jsonify(QuestionResponse.from_orm(question).dict())


@questions_bp.route('/<int:id>', methods=['DELETE'])
def delete_question(id):
    question = Question.query.get_or_404(id)
    db.session.delete(question)
    db.session.commit()
    return {"message": "Question deleted"}, 200
