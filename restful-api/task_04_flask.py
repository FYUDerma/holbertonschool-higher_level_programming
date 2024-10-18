#!/usr/bin/python3
from flask import Flask, jsonify, request


app = Flask(__name__)
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    return "OK"


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
    username = data.get('username', None)
    name = data.get('name', None)
    age = data.get('age', None)
    city = data.get('city', None)

    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = {
        "username": username,
        "name": name,
        "age": age,
        "city": city
    }
    return jsonify({'message': 'User  added', 'user': users[username]}), 201


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


if __name__ == "__main__":
    app.run()
