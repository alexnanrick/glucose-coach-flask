"""
    Author: Alex Kiernan

    Desc: Facts routes
"""
from app import app, auth
from flask import jsonify, abort
from ..resources.user import User
from ..resources.fact import Fact


@app.route('/glucose_coach/api/v1.0/facts/<string:user_name>/latest', methods=['GET'])
@auth.login_required
def read_fact(user_name):
    user = User.query.filter_by(username=user_name).first()

    if user is None:
        abort(404)

    fact = Fact.query.filter_by(user_id=user.id).order_by(Fact.pf_date.desc(), Fact.pf_time_of_day.desc()).first()

    if fact is None:
        abort(404)

    return jsonify(fact.serialize())


@app.route('/glucose_coach/api/v1.0/facts/<string:user_name>', methods=['GET'])
@auth.login_required
def read_all_facts(user_name):
    user = User.query.filter_by(username=user_name).first()

    if user is None:
        abort(404)

    data = Fact.query.filter_by(user_id=user.id).order_by(Fact.pf_date.desc(), Fact.pf_time_of_day.desc()).all()
    data_all = []

    if data is None:
        return 204

    for fact in data:
        data_all.append(fact.serialize())

    return jsonify(data_all)
