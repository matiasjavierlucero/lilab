from flask import Flask, request, jsonify
from app import app, db, fake
import random
from marshmallow import fields
from .models_client import Client, client_schema


@app.route('/clients', methods=["GET"])
def clients():
    result = client_schema.dump(Client.query.all(),many=True)
    return jsonify(result)

@app.route('/populate_table')
def populate_table():
    clients = db.session.query(Client).all()
    if len(clients)<1:
        for _ in range(50):
            name = fake.name()
            risk = random.randint(1,10)
            new_client = Client(name, risk)
            db.session.add(new_client)
            db.session.commit()

    return clients()