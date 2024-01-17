from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from urllib.parse import quote_plus
from pymongo import MongoClient
import pymongo
from malicious_url_detection_and_fraud_phone_number_detection import (
    predict_url,
    predict_phone_number,
)
app = Flask(__name__)
CORS(app)
global_username = quote_plus('khushikasera001')
global_password = quote_plus('Khushi@09vidit')

#CONNECTION_STRING = f"mongodb+srv://{global_username}:{global_password}@cluster0.4ocbcae.mongodb.net/test?retryWrites=true&w=majority"
CONNECTION_STRING = "mongodb://localhost:27017"

client = MongoClient(CONNECTION_STRING) 
db = client['scam-buster'] 
collection = db['users'] 

@app.route('/') 
def hello_world(): 
    return 'Hello, World!'

@app.route('/apitest', methods=['GET'])
def apitest():
    return jsonify({'message': 'Api tested successfully'}), 201

# Submit API
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    print(data)
    username = data.get('username')
    email = data.get('email')
    phone = data.get('phone')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400

    #hashed_password = generate_password_hash(password, method='sha256')

    user_data = {
        'username': username,
        'email':email,
        'phone':phone,
        'password': password
    }
    print(CONNECTION_STRING)
    print(client)
    print(db)
    print(collection)
    #users_collection = mongo.db.users
    collection.insert_one(user_data)

    return jsonify({'message': 'User registered successfully'}), 201

# Login API
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400

    #users_collection = mongo.db.users
    user = collection.find_one({'username': username})
    print(user)
    if user and user['password']== password:
        user['_id'] = str(user['_id'])
        return jsonify({'message': 'Login successful','user': user}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

#url test
@app.route('/urlCheck', methods=['POST'])
def urlCheck():
    data = request.get_json()
    result = predict_url(data)

    return jsonify({'message': 'URL is Valid', 'result': result}), 201

#phone test
@app.route('/phoneCheck', methods=['POST'])
def phoneCheck():
    data = request.get_json()
    result = predict_phone_number(data)
    return jsonify({'message': 'PHONE is Valid', 'result': result}), 201

if __name__ == '__main__':
    app.run(debug=True)
