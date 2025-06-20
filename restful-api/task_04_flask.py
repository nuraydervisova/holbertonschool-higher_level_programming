from flask import Flask, jsonify, request

app = Flask(__name__)

# Uygulama içi kullanıcı verisi
users = {
    # "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(list(users.keys()))

@app.route('/status', methods=['GET'])
def status():
    return "OK"

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run()
