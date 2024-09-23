from init import db, ma
from marshmallow import fields

class Card(db.model):
    __tablename__ = "cards"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullabul=False)
    description = db.Column(db.String)
    status = db.Column(db.String)
    priority = db.Column(db.String)
    data = db.Column(db.Date) #created date

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

    user = db.relationship('Model_name', back_populates ='cards')


class CardSchema(ma.Schema)
    user = fields.Nested('UserSchema', only = ["id", "name", "email"])

    class Meta:
        fields = ("id", "title", "description", "status", "priority", "date", "user_id")



card_schema = CardSchema()
cards_schema = CardSchema(many=True)




