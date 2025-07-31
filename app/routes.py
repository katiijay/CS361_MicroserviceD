from app import app
from flask import jsonify, request

test_payload = [
    {
  'temperature': {
    'min': 58,
    'max': 72,
    'scale': 'fahrenheit'
  },
  'cloud': {
    'coverage': 15,
    'scale': 'percentage'
  },
  'precipitation': {
    'type': 'rain',
    'amount': 5,
    'scale': 'inches'
  },
 'wind': {
    'speed': 10,
    'scale': 'mph'
  }
}
]

@app.route('/weather')
def get_incomes():
    return jsonify(test_payload)
