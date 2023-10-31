from api import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


class Admin(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow())
    updated_at = db.Column(db.DateTime(), onupdate=datetime.utcnow())
    
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow())
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())
    admin_id = db.Column(db.Integer, db.ForeignKey("admins.id"))

class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)
    coordinates = db.Column(db.String)
    population = db.Column(db.Integer)
    more_details = db.Column(db.String)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow())
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())

class Disease(db.Model):
    __tablename__ = "diseases"

    id = db.Column(db.Integer, primary_key=True)
    disease_name = db.Column(db.String(50), index=True)
    description = db.Column(db.Text)
    symptoms = db.Column(db.Text)
    prevention = db.Column(db.Text)
    treatment = db.Column(db.Text)
    num_of_cases = db.Column(db.Integer)

class Disease_Location(db.Model):
    __tablename__ = "disease_locations"

    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    disease_id = db.Column(db.Integer, db.ForeignKey('diseases.id'))
    disease = db.Column(db.String)
    location = db.Column(db.String)
    cases = db.Column(db.Integer)


class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    review = db.Column(db.Text)

class Donation(db.Model):
    __tablename__ = 'donations'
    id = db.Column(db.Integer, primary_key=True)
    donor_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    recipient_location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)

