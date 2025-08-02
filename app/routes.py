from app import app
from flask import jsonify, request
from .calls.weathercall import get_weather

@app.route('/forecast', methods=['GET'])
def get_forecast():
    latitude = request.args.get('lat')
    longitude = request.args.get('long')
    date = request.args.get('date')
    results = get_weather(latitude, longitude, date)
    #if date < datetime.today():
    #    raise ValueError('Cannot retrieve a forecast for a day that has already occurred')
    return jsonify(results)