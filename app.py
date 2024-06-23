
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



if __name__ == '__main__':
    app.run(debug=True, port=5000)
