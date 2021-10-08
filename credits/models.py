from app import db, ma
from marshmallow import fields
from clients.models_client import Client, ClientSchema

class Credits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    idClient = db.Column(db.Integer,  db.ForeignKey('client.id'))
    client= db.relationship('Client',backref='credits')
    
    def __init__(self,quantity,idClient):
        self.quantity=quantity
        self.idClient=idClient 
        

class CreditsSchema(ma.Schema):
    idCredits = fields.Integer(dump_only=True)
    quantity = fields.String() 
    client=fields.Nested('ClientSchema', many=True)

credit_schema = CreditsSchema()