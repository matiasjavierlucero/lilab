from app import db, ma, fake
from marshmallow import fields


class Client(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100))
    risk = db.Column(db.Integer)
    debts = db.Column(db.Float(10,2))
   
    def __init__(self, name, risk, debts):
        self.name = name
        self.risk = risk
        self.debts = debts
  
class ClientSchema(ma.Schema):
    idClient = fields.Integer(dump_only=True)
    nameClient = fields.String() 
    riskClient = fields.Integer() 
    debtsClient = fields.Float()
    
client_schema = ClientSchema()