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
    """
    Returns a welcome message to the Flask API.

    Returns:
        str: "Welcome to the Flask API!"
    """
    return "Welcome to the Flask API!"


@app.route("/data", methods=['GET'])
def data():
    """
    Returns a list of all user usernames.

    Returns:
        json: A JSON response containing a list of usernames.
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """
    Returns the status of the API.

    Returns:
        str: "OK"
    """
    return "OK"


@app.route("/users/<username>")
def show_user_profile(username):
    """
    Returns the user profile for the given username.

    Args:
        username (str): The username to retrieve.

    Returns:
        json: A JSON response containing the user profile if found, otherwise an error message.
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User  not found"})


@app.route("/add_user", methods=['POST'])
def add_user():
    """
    Adds a new user to the system.

    Args:
        data (dict): A dictionary containing the user data.

    Returns:
        json: A JSON response containing a success message and the added user data if successful, otherwise an error message.
    """
    data = request.get_json()
    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    username = data['username']
    if username in users:
        return jsonify({'message': 'User  already exists'})
    else:
        users[username] = data
        return jsonify({'message': 'User  added', 'user': data})


if __name__ == "__main__":
    app.run(debug=True)
