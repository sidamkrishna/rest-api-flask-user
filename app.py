from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory user data
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"}
}

# Get all users
@app.route("/users", methods=["GET"])
def get_all_users():
    return jsonify(users)

# Get a specific user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    if user_id in users:
        return jsonify({user_id: users[user_id]})
    return jsonify({"error": "User not found"}), 404

# Add a new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    user_id = data["id"]

    if user_id in users:
        return jsonify({"error": "User already exists"}), 400

    users[user_id] = {
        "name": data["name"],
        "email": data["email"]
    }

    return jsonify({user_id: users[user_id]}), 201

# Update an existing user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    users[user_id]["name"] = data.get("name", users[user_id]["name"])
    users[user_id]["email"] = data.get("email", users[user_id]["email"])

    return jsonify({user_id: users[user_id]})

# Delete a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        deleted = users.pop(user_id)
        return jsonify({"deleted": deleted})
    return jsonify({"error": "User not found"}), 404

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
