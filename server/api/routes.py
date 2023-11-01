from api import app, db
from flask_restx import Resource, Namespace
from .models import Admin, User, Location, Disease, Donation, Review, Disease_Location
from .api_models import ( admin_model, user_model, location_model, disease_model, disease_location_model, review_model, donation_model, user_input_model, location_input_model, disease_input_model, donation_input_model, review_input_model)
from werkzeug.security import generate_password_hash, check_password_hash

ns = Namespace("/")

#ADMIN ROUTES
@ns.route("/admins")
class Admins(Resource):
    @ns.marshal_with(admin_model)
    def get(self):
        admins = Admin.query.all()
        return admins, 200
  
@ns.route("/admins/<int:id>")
class AdminsId(Resource):
    @ns.marshal_with(admin_model)
    def get(self, id):
        admin = Admin.query.filter_by(id=id).first()
        if admin:
            return admin, 200
        else:
            return {"error": "Admin not found"}, 404


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
    @ns.marshal_with(admin_model)
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            return user, 200
        else:
            return {"error": "User not found"}, 404
        
    #patch users
    @ns.expect(user_input_model)
    @ns.marshal_with(user_model)
    def patch(self, id):
        hashed_password = generate_password_hash(password=ns.payload["password_hash"])
        user = User.query.filter_by(id=id).first()
        if user:
            for attr in ns.payload:
                if attr == "password_password_hash":
                    setattr(user, attr, hashed_password)
                else:
                    setattr(user, attr, ns.payload[attr])
            db.session.add(user)
            db.session.commit()
            return user, 200
        else:
            return {"error": "User not found"}, 404
        
    #delete users
    def delete(self, id):
        users = User.query.filter_by(id=id).first()
        if users:
            db.session.delete(users)
            db.session.commit()
            return {}, 204
        else:
            return {"error": "Users not found"}, 404
        
        

#LOCATION ROUTES
@ns.route("/location")
class Locations(Resource):
    @ns.marshal_with(location_model)
    def get(self):
        locations = Location.query.all()
        return locations, 200
    
    #locations posts
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
    @ns.marshal_with(location_model)
    def get(self, id):
        locations = Location.query.filter_by(id=id).first()
        if locations:
            return locations, 200
        else:
            return {"error": "Location not found"}, 404
        
    #patch location
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
    @ns.marshal_with(disease_model)
    def get(self):
        diseases = Disease.query.all()
        return diseases, 200
    
    #Disease Input
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
    @ns.marshal_with(disease_model)
    def get(self, id):
        diseases = Disease.query.filter_by(id=id).first()
        if diseases:
            return diseases, 200
        else:
            return {"error": "Disease not found"}, 404
        
    #Patching diseases
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
    @ns.marshal_with(donation_model)
    def get(self):
        donations = Donation.query.all()
        return donations, 200
    
    #input donations
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
    @ns.marshal_with(review_model)
    def get(self):
        reviews = Review.query.all()
        return reviews, 200
    
    #reviews posts
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
    @ns.marshal_with(review_model)
    def get(self, id):
        reviews = Review.query.filter_by(id=id).first()
        if reviews:
            return reviews, 200
        else:
            return {"error": "Review not found"}, 404
        
    #Pactch reviews
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
    def delete(self, id):
        reviews = Review.query.filter_by(id=id).first()
        if reviews:
            db.session.delete(reviews)
            db.session.commit()
            return {}, 204
        else:
            return {"error": "Review not found"}, 404
