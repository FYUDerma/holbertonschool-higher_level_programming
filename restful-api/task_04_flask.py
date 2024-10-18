#!/usr/bin/python3
from flask import Flask, jsonify, request


app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """Return a welcome message for the Flask API."""
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """Return the status of the API."""
    return "OK"


@app.route("/users/<username>")
def show_user_profile(username):
    """Show the user profile for a given username.

    Args:
        username (str): The username of the user to retrieve.

    Returns:
        JSON: A JSON object containing user details or an error message.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=['POST'])
def add_user():
    """Add a new user to the users dictionary.

    The request must contain a JSON body with the following fields:
    - username (str): The username of the user.
    - name (str): The name of the user.
    - age (int): The age of the user.
    - city (str): The city of the user.

    Returns:
        JSON: A message indicating the user was added or an error message.
    """
    data = request.get_json()
    username = data.get('username')
    name = data.get('name')
    age = data.get('age')
    city = data.get('city')

    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = {
        "username": username,
        "name": name,
        "age": age,
        "city": city
    }
    return jsonify({'message': 'User added', 'user': users[username]}), 201


@app.route("/data")
def data():
    """Return a list of all usernames in the users dictionary.

    Returns:
        JSON: A list of usernames.
    """
    return jsonify(list(users.keys()))


if __name__ == "__main__":
    app.run()