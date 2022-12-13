from flask import Flask, request
from app_api import db, app
from app_api.models import Recipe


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/skull', methods=['GET'])
def skull():
    return 'Hi! This is the BACKEND SKULL! 💀'

@app.routes('/recipes', methods=['POST'])
def create_recipe():
    name = request.json['name']
    rating = request.json['rating']
    ingredients = request.json['ingredients']
    steps = request.json['steps']
    favorite = request.json['favorite']
    recipe = Recipe(name, rating, ingredients, steps, favorite)
    db.session.add(recipe)
    db.session.commit()
    return format_recipe(recipe)

@app.routes('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return {'recipes': [format_recipe(recipe) for recipe in recipes]}

@app.routes('/recipes/<int:id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipe.query.get(id)
    return format_recipe(recipe)

@app.routes('/recipes/<int:id>', methods=['PUT'])
def update_recipe(id):
    recipe = Recipe.query.get(id)
    recipe.name = request.json['name']
    recipe.rating = request.json['rating']
    recipe.favorite = request.json['favorite']
    db.session.commit()
    return format_recipe(recipe)

@app.routes('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    return format_recipe(recipe)

def format_recipe(recipe):
    return {
        'id': recipe.id,
        'name': recipe.name,
        'rating': recipe.rating,
        'ingredients': recipe.ingredients,
        'steps': recipe.steps,
        'favorite': recipe.favorite,
        'created_at': recipe.created_at
    }