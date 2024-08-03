from flask import Blueprint, request
from app.models import db, Question

questions_bp = Blueprint('questions', __name__, url_prefix='/questions')


@questions_bp.route('/', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    return {"questions": [str(question) for question in questions]}


@questions_bp.route('/', methods=['POST'])
def create_question():
    data = request.json
    new_question = Question(text=data['text'])
    db.session.add(new_question)
    db.session.commit()
    return {"message": "Question created"}, 201


@questions_bp.route('/<int:id>', methods=['GET'])
def get_question(id):
    question = Question.query.get_or_404(id)
    return {"question": str(question)}


@questions_bp.route('/<int:id>', methods=['PUT'])
def update_question(id):
    data = request.json
    question = Question.query.get_or_404(id)
    question.text = data['text']
    db.session.commit()
    return {"message": "Question updated"}


@questions_bp.route('/<int:id>', methods=['DELETE'])
def delete_question(id):
    question = Question.query.get_or_404(id)
    db.session.delete(question)
    db.session.commit()
    return {"message": "Question deleted"}
