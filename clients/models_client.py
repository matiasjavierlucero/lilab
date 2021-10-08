from app import db, ma, fake
from marshmallow import fields


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    risk = db.Column(db.Integer)
   
    def __init__(self, name, risk):
        self.name = name
        self.risk = risk

  
class ClientSchema(ma.Schema):
    idClient = fields.Integer(dump_only=True)
    nameClient = fields.String() 
    riskClient = fields.Integer() 

client_schema = ClientSchema()