from flask import Flask, request, jsonify
from app import app
import random
from marshmallow import fields
from .models import Credits, CreditsSchema, credit_schema


@app.route('/credits', methods=["POST"])
def credits():
    result = credit_schema.dump(Credits.query.all(),many=True)
    return jsonify(result)

@app.route('/credits/<id>', methods=["POST"])
def credit_id(id):
    result = credit_schema.dump(Credits.query.filter(id=id),many=True)
    return jsonify(result)
