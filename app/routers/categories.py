from flask import Blueprint, request
from app.models import db, Category

categories_bp = Blueprint('categories', __name__, url_prefix='/categories')


@categories_bp.route('/', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return {"categories": [str(category) for category in categories]}


@categories_bp.route('/', methods=['POST'])
def create_category():
    data = request.json
    new_category = Category(name=data['name'])
    db.session.add(new_category)
    db.session.commit()
    return {"message": "Category created"}, 201
