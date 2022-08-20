from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favorites')
def favorites():
    favorites = ['cookies', 'chocolate','coke', 'sleep','cheetos']
    return render_template('favorites.html', favorites=favorites)