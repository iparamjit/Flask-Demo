from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify({'message': f'Hello, {name}!'})
