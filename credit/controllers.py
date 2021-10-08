from flask import Flask, request, jsonify
from app import app
import random
from marshmallow import fields
from .models import credit, credit_schema


@app.route('/credit', methods=["POST"])
def credit():
    return jsonify(credit_schema.dump(credit.query.all(), many=True))

@app.route('/credit/<id>', methods=["POST"])
def credit_id(id):
   return (credit_schema.dump(credit.query.filter(id=id), many=True))
