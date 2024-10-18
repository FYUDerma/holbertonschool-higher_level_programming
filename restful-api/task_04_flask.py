#!/usr/bin/python3
from flask import Flask, jsonify, request


app = Flask(__name__)
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    return "OK"


@app.route("/data", methods=['GET'])
def data():
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def show_user_profile(username):
    user_info = users.get(username)
    if user_info:
        return jsonify(user_info)
    else:
        return jsonify({"error": "User  not found"}), 404


@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.get_json()

    if not "username" in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']
    if username in users:
        return jsonify({'message': 'User  already exists'})
    else:
        users[username] = data
        return jsonify({'message': 'User  added', 'user': data})


if __name__ == "__main__":
    app.run(debug=True)
