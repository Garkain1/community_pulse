from flask import Blueprint, request, jsonify
from app.models import db, Category
from pydantic import ValidationError
from app.schemas.question import CategoryBase, CategoryResponse

categories_bp = Blueprint('categories', __name__, url_prefix='/categories')


@categories_bp.route('/', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    results = [CategoryResponse.from_orm(category).dict() for category in categories]
    return jsonify(results)


@categories_bp.route('/<int:id>', methods=['GET'])
def get_category(id):
    category = Category.query.get_or_404(id)
    return jsonify(CategoryResponse.from_orm(category).dict())


@categories_bp.route('/', methods=['POST'])
def create_category():
    try:
        data = CategoryBase(**request.get_json())
    except ValidationError as e:
        return jsonify(e.errors()), 400

    new_category = Category(name=data.name)
    db.session.add(new_category)
    db.session.commit()

    return jsonify(CategoryResponse.from_orm(new_category).dict()), 201


@categories_bp.route('/<int:id>', methods=['PUT'])
def update_category(id):
    try:
        data = CategoryBase(**request.get_json())
    except ValidationError as e:
        return jsonify(e.errors()), 400

    category = Category.query.get_or_404(id)
    category.name = data.name
    db.session.commit()

    return jsonify(CategoryResponse.from_orm(category).dict())


@categories_bp.route('/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return {"message": "Category deleted"}, 200
