from app import db, ma
from marshmallow import fields
from clients.models_client import Client, ClientSchema

class Credit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    idClient = db.Column(db.Integer,  db.ForeignKey('client.id'))
    approbe = db.Column(db.Boolean, default="0")
    client= db.relationship('Client',backref='credit')
    
    def __init__(self,quantity,idClient):
        self.quantity=quantity
        self.idClient=idClient 
        

class creditSchema(ma.Schema):
    idcredit = fields.Integer(dump_only=True)
    quantity = fields.String() 
    approbe=fields.Boolean()
    client=fields.Nested('ClientSchema', many=True)

credit_schema = creditSchema()