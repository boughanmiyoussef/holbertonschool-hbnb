
from flask import Flask, request, jsonify, make_response
from datetime import datetime
import uuid
from data_manager import data_manager

app = Flask(__name__)

# User Routes
@app.route('/users', methods=['GET', 'POST'], strict_slashes=False)
def manage_users():
    if request.method == 'GET':
        return jsonify(data_manager.get_all('users'))

    if request.method == 'POST':
        data = request.get_json()
        if not data or 'email' not in data or 'first_name' not in data or 'last_name' not in data:
            return make_response(jsonify({'error': 'Mandatory'}), 400)
        data['id'] = str(uuid.uuid4())
        data['created_at'] = data['updated_at'] = datetime.now().isoformat()
        data_manager.save('users', data['id'], data)
        return make_response(jsonify(data), 201)

@app.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def manage_user(user_id):
    user = data_manager.get('users', user_id)
    if not user:
        return make_response(jsonify({'error': 'User not found'}), 404)

    if request.method == 'GET':
        return jsonify(user)

    if request.method == 'PUT':
        data = request.get_json()
        if not data:
            return make_response(jsonify({'error': 'No data provided'}), 400)
        data['id'] = user_id
        data['updated_at'] = datetime.now().isoformat()
        data_manager.update('users', user_id, data)
        return jsonify(data)

    if request.method == 'DELETE':
        data_manager.delete('users', user_id)
        return make_response('User Successfully Deleted', 204)


    

if __name__ == '__main__':
    app.run(debug=True, port=5000)
