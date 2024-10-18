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
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User  not found"}), 404


@app.route("/add_user", methods=['POST'])
def post_register():
    """Add user"""
    if request.is_json:
        data = request.get_json()
        username = data.get("username")
        name = data.get("name")
        age = data.get("age")
        city = data.get("city")

        if not username:
            return jsonify({"error": "Username is required"}), 400

        users[username] = {
            "username": username,
            "name": name,
            "age": age,
            "city": city
        }
        return jsonify({"message": "User added",
                        "user": users[username]
                        }), 201
    else:
        return jsonify({"error": "Request must be JSON"}), 400


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


if __name__ == "__main__":
    app.run()
