from app import app
from flask import jsonify, request
from .calls.activities import get_activities, get_all_activities

@app.route('/activities', methods=['GET'])
def get_park_activities():
    parkcode = request.args.get('parkcode')
    results = get_activities(parkcode)
    return jsonify(results)

@app.route('/allactivities', methods=['GET'])
def get_all_park_activities():
    results = get_all_activities()
    return jsonify(results)