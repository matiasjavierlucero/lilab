from flask import Flask, request, jsonify
from app import app, db, fake
import random
from marshmallow import fields
from clients.models_client import Client
from credit.models import credit, credit_schema


@app.route('/credit/<id>', methods=["GET"])
def credit_for_client(id):
    credit = db.session.query(credit).filter(id=id).first()
    if credit.quantity>50000:
        return {
            "Client debts" : credit.clients.debts,
            "Client Risk" : credit.clients.risk 
        }
    else:
        return jsonify(credit_schema.dump(credit, many=True))


@app.route('/credit/<id>', methods=["GET"])
def credit_approbe(id):
    credit = db.session.query(credit).filter(id=id).first()
    credit.approbe = True
    db.session.commit()
    return jsonify(credit_schema.dump(credit, many=True))

