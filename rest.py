from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# In-memory user storage
users = {}
next_id = 1

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values()))

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        abort(404)
    return jsonify(user)

@app.route('/users', methods=['POST'])
def create_user():
    global next_id
    data = request.get_json()
    if not data or 'name' not in data:
        abort(400)
    user = {'id': next_id, 'name': data['name']}
    users[next_id] = user
    next_id += 1
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if not data or 'name' not in data:
        abort(400)
    user = users.get(user_id)
    if not user:
        abort(404)
    user['name'] = data['name']
    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        abort(404)
    del users[user_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)