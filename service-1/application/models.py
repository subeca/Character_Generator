from application import db

class Hogwarts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hogwarts_house = db.Column(db.String(50), nullable=False)
    hogwarts_personality_trait = db.Column(db.String(50), nullable=False)
    hogwarts_subject = db.Column(db.String(600), nullable=False)