#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Pet, Owner

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Welcome home! Search a pet id [1-100]</h1>'

@app.route('/pets/<int:id>')
def get_pet(id):
    pet = Pet.query.filter(Pet.id == id).first()
    if not pet:
        body = "<h1>404!!! pet not found :(</h1>"
        return make_response(body, 404)
    else:
        owner = Owner.query.filter(Owner.id == pet.owner_id).one()
        body = f'''
        <h1>
        Name: {pet.name}
        <br />
        Species: {pet.species}
        <br />
        Owner: {owner.name}
        </h1>
        '''
        return make_response(body, 202)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
