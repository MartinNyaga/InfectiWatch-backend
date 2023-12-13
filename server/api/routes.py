import re
from api import app, db
from flask_restx import Resource, Namespace
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
import jwt
from .models import User, Location, Disease, Donation, Review, Disease_Location, Emergency
from .api_models import (  user_model, location_model, disease_model, disease_location_model, review_model, donation_model, user_input_model, location_input_model, disease_input_model, donation_input_model, review_input_model, emergency_model, emergency_input_model, user_login_model)
from werkzeug.security import generate_password_hash, check_password_hash

authorizations = {
    "jsonWebToken": {"type": "apiKey", "in": "header", "name": "Authorization"}
}


ns = Namespace("/", authorizations=authorizations)

#ADMIN ROUTES
# @ns.route("/roles")
# class Roles(Resource):
#     method_decorators = [jwt_required()]

#     @ns.doc(security="jsonWebToken")
#     @ns.marshal_with(role_model)
#     def get(self):
#         roles = Role.query.all()
#         return roles, 200
  
# @ns.route("/admins/<int:id>")
# class RolesId(Resource):
#     method_decorators = [jwt_required()]

#     @ns.doc(security="jsonWebToken")
#     @ns.marshal_with(role_model)
#     def get(self, id):
#         roles = Role.query.filter_by(id=id).first()
#         if roles:
#             return roles, 200
#         else:
#             return {"error": "roles not found"}, 404


#USERS ROUTES
@ns.route("/users")
class Users(Resource):
    
    @ns.marshal_with(user_model)
    def get(self):
        users = User.query.all()
        return users, 200
    
    #post users
    @ns.expect(user_input_model)
    @ns.marshal_with(user_model)
    def post(self):
        try:
            email = ns.payload["email"]
            
            # Validate email
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email): # checks if the structure of the email is valid or not.
                return {"error": "Invalid email format"}, 400

            
            hashed_password = generate_password_hash(password=ns.payload["password_hash"])
            new_user = User(
                username=ns.payload["username"],
                email=ns.payload["email"],
                password_hash=hashed_password,
            )
            db.session.add(new_user)
            db.session.commit()

            return new_user, 201
        except Exception as e:
            print(e.args)
            return {"error": f"User registration error {str(e)}"}, 400
    
@ns.route("/users/<int:id>")
class UsersId(Resource):
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    @ns.marshal_with(user_model)
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            return user, 200
        else:
            return {"error": "User not found"}, 404
        
    #patch users
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    @ns.expect(user_input_model)
    @ns.marshal_with(user_model)
    def patch(self, id):
        hashed_password = generate_password_hash(password=ns.payload["password_hash"])
        user = User.query.filter_by(id=id).first()
        if user:
            for attr in ns.payload:
                if attr == "password_hash":
                    setattr(user, attr, hashed_password)
                else:
                    setattr(user, attr, ns.payload[attr])
            db.session.add(user)
            db.session.commit()
            return user, 200
        else:
            return {"error": "User not found"}, 404
        
    #delete users
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    def delete(self, id):
        users = User.query.filter_by(id=id).first()
        if users:
            db.session.delete(users)
            db.session.commit()
            return {}, 204
        else:
            return {"error": "Users not found"}, 404
        
#User Log In
@ns.route("/login")
class UserLoginResource(Resource):
    @ns.expect(user_login_model)
    def post(self):

        user = User.query.filter_by(username=ns.payload["username"]).first()
        if not user:
            return {"error": "User does not exist"}, 401
        if not check_password_hash(user.password_hash, ns.payload["password_hash"]):
            return {"error": "Incorrect password, Try Again"}, 401
        user_dic = {
            "id": user.id,
            "username": user.username,
        }
        return {"access_token": create_access_token(user_dic)}
        
        

#LOCATION ROUTES
@ns.route("/location")
class Locations(Resource):
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    @ns.marshal_with(location_model)
    def get(self):
        locations = Location.query.all()
        return locations, 200
    
    #locations posts
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    @ns.expect(location_input_model)
    @ns.marshal_with(location_model)
    def post(self):
        new_location = Location(
            name=ns.payload["name"],
            coordinates=ns.payload["coordinates"],
            population=ns.payload["population"],
            more_details=ns.payload["more_details"],
        )
        db.session.add(new_location)
        db.session.commit()

        return new_location, 201
    
@ns.route("/location/<int:id>")
class LocationsId(Resource):
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    @ns.marshal_with(location_model)
    def get(self, id):
        locations = Location.query.filter_by(id=id).first()
        if locations:
            return locations, 200
        else:
            return {"error": "Location not found"}, 404
        
    #patch location
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    @ns.expect(location_input_model)
    @ns.marshal_with(location_model)
    def patch(self, id):
        location = Location.query.get(id)
        if location:
            for attr in ns.payload:
                setattr(location, attr, ns.payload[attr])
            db.session.add(location)
            db.session.commit()
            return location, 200
        else:
            return {"error": "Location not found"}, 404
        
    #delete locations
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    def delete(self, id):
        locations = Location.query.filter_by(id=id).first()
        if locations:
            db.session.delete(locations)
            db.session.commit()
            return {}, 204
        else:
            return {"error": "Location not found"}, 404
        
#DISEASES ROUTES
@ns.route("/diseases")
class Diseases(Resource):
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    @ns.marshal_with(disease_model)
    def get(self):
        diseases = Disease.query.all()
        return diseases, 200
    
    #Disease Input
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    @ns.expect(disease_input_model)
    @ns.marshal_with(disease_model)
    def post(self):
        new_disease = Disease(
            disease_name=ns.payload["disease_name"],
            description=ns.payload["description"],
            symptoms=ns.payload["symptoms"],
            prevention=ns.payload["prevention"],
            treatment=ns.payload["treatment"],
            num_of_cases=ns.payload["num_of_cases"],
        )
        db.session.add(new_disease)
        db.session.commit()

        return new_disease, 201
    

@ns.route("/diseases/<int:id>")
class DiseasesId(Resource):
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    @ns.marshal_with(disease_model)
    def get(self, id):
        diseases = Disease.query.filter_by(id=id).first()
        if diseases:
            return diseases, 200
        else:
            return {"error": "Disease not found"}, 404
        
    #Patching diseases
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    @ns.expect(disease_input_model)
    @ns.marshal_with(disease_model)
    def patch(self, id):
        diseases = Donation.query.get(id)
        if diseases:
            for attr in ns.payload:
                setattr(diseases, attr, ns.payload[attr])
            db.session.add(diseases)
            db.session.commit()
            return diseases, 200
        else:
            return {"error": "Diseases not found"}, 404
        
    #delete diseases
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    def delete(self, id):
        diseases = Disease.query.filter_by(id=id).first()
        if diseases:
            db.session.delete(diseases)
            db.session.commit()
            return {}, 204
        else:
            return {"error": "Disease not found"}, 404
        
#DONATIONS ROUTES
@ns.route("/donations")
class Donations(Resource):
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    @ns.marshal_with(donation_model)
    def get(self):
        donations = Donation.query.all()
        return donations, 200
    
    #input donations
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    @ns.expect(donation_input_model)
    @ns.marshal_with(donation_model)
    def post(self):
        new_donation = Donation(
            donor_user_id=ns.payload["donor_user_id"],
            recipient_location_id=ns.payload["recipient_location_id"],
            amount=ns.payload["amount"],
        )
        db.session.add(new_donation)
        db.session.commit()

        return new_donation, 201
    
@ns.route("/donations/<int:id>")
class DonationsId(Resource):
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    @ns.marshal_with(donation_model)
    def get(self, id):
        donations = Donation.query.filter_by(id=id).first()
        if donations:
            return donations, 200
        else:
            return {"error": "Donation not found"}, 404
        
    
        
#REVIEWS ROUTES
@ns.route("/reviews")
class Reviews(Resource):
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    @ns.marshal_with(review_model)
    def get(self):
        reviews = Review.query.all()
        return reviews, 200
    
    #reviews posts
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    @ns.expect(review_input_model)
    @ns.marshal_with(review_model)
    def post(self):
        new_review = Review(
            user_id=ns.payload["user_id"],
            location_id=ns.payload["location_id"],
            review=ns.payload["review"],
        )
        db.session.add(new_review)
        db.session.commit()

        return new_review, 201
    
@ns.route("/reviews/<int:id>")
class ReviewsId(Resource):
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    @ns.marshal_with(review_model)
    def get(self, id):
        reviews = Review.query.filter_by(id=id).first()
        if reviews:
            return reviews, 200
        else:
            return {"error": "Review not found"}, 404
        
    #Patch reviews
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    @ns.expect(review_input_model)
    @ns.marshal_with(review_model)
    def patch(self, id):
        reviews = Review.query.get(id)
        if reviews:
            for attr in ns.payload:
                setattr(reviews, attr, ns.payload[attr])
            db.session.add(reviews)
            db.session.commit()
            return reviews, 200
        else:
            return {"error": "Diseases not found"}, 404

    #delete review
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    def delete(self, id):
        reviews = Review.query.filter_by(id=id).first()
        if reviews:
            db.session.delete(reviews)
            db.session.commit()
            return {}, 204
        else:
            return {"error": "Review not found"}, 404

#Emergency Route
@ns.route("/emergencies")
class Emergencies(Resource):
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    @ns.marshal_with(emergency_model)
    def get(self):
        emergencies = Emergency.query.all()
        return emergencies, 200
    
     #emergencies posts
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    @ns.expect(emergency_input_model)
    @ns.marshal_with(emergency_model)
    def post(self):
        new_emergency = Emergency(
            sender_user_id=ns.payload["sender_user_id"],
            sender_location=ns.payload["sender_location"],
            condition=ns.payload["condition"],
        )
        db.session.add(new_emergency)
        db.session.commit()

        return new_emergency, 201
    

@ns.route("/emergencies/<int:id>")
class EmergenciesId(Resource):
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    @ns.marshal_with(emergency_model)
    def get(self, id):
        emergencies = Emergency.query.filter_by(id=id).first()
        if emergencies:
            return emergencies, 200
        else:
            return {"error": "Emergency not found"}, 404
        
    #Patch emergencies
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    @ns.expect(emergency_input_model)
    @ns.marshal_with(emergency_model)
    def patch(self, id):
        emergencies = Emergency.query.get(id)
        if emergencies:
            for attr in ns.payload:
                setattr(emergencies, attr, ns.payload[attr])
            db.session.add(emergencies)
            db.session.commit()
            return emergencies, 200
        else:
            return {"error": "Emergencies not found"}, 404
        
    #delete emergencies
    method_decorators = [jwt_required()]

    @ns.doc(security="jsonWebToken")
    def delete(self, id):
        emergencies = Emergency.query.filter_by(id=id).first()
        if emergencies:
            db.session.delete(emergencies)
            db.session.commit()
            return {}, 204
        else:
            return {"error": "Emergency not found"}, 404