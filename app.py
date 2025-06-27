from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user data (each user is a dict)
users = []

# Helper function to find a user by ID
def find_user(user_id):
    return next((user for user in users if user["id"] == user_id), None)

# Route: Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# Route: Get a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = find_user(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# Route: Add a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data.get("id") or not data.get("name"):
        return jsonify({"error": "ID and name are required"}), 400
    if find_user(data["id"]):
        return jsonify({"error": "User with this ID already exists"}), 400
    users.append(data)
    return jsonify({"message": "User created", "user": data}), 201

# Route: Update a user by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = find_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    user.update(data)
    return jsonify({"message": "User updated", "user": user}), 200

# Route: Delete a user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = find_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    users.remove(user)
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
