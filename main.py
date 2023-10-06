import json

from flask import Flask, request, jsonify

with open('data.json') as f:
      data = json.load(f)
      
app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    return jsonify(data)