"""
    Author: Alex Kiernan

    Desc: Handle errors
"""
from app import app
from flask import jsonify, make_response


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(500)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 500)
