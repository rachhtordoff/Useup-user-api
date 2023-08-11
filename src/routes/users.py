from flask import Blueprint, jsonify
from src.models import User
from flask_jwt_extended import create_access_token, jwt_required

users_blueprint = Blueprint('users', __name__)

@app.route('/signup', methods=['POST'])
def signup():
    print('YESHSHSH')
    data = request.get_json()
    print(data)
    new_user = User(data)
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created!"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and user.check_password(data['password']):
        token = create_access_token(identity=user.email)
        return jsonify(access_token=token), 200
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected_route():
    return jsonify({"message": "This is a protected route!"})

