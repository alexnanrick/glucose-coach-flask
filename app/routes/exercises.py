from app import app, db, auth
from flask import jsonify, request, abort
from ..resources.exercise import Exercise

@app.route('/glucose_coach/api/v1.0/exercises', methods=['GET'])
@auth.login_required
def read_all_exercises():
    data = Exercise.query.all()
    data_all = []

    for exercise in data:
        data_all.append(exercise.serialize())

    return jsonify(exercises=data_all)