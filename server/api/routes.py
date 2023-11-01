from api import app, db
from flask_restx import Resource, Namespace
from .models import Admin, User, Location, Disease, Donation, Review, Disease_Location
from .api_models import ( admin_model, user_model, location_model, disease_model, disease_location_model, review_model, donation_model, user_input_model, location_input_model)
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
        admins = User.query.all()
        return admins, 200
    
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
        

#LOCATION ROUTES
@ns.route("/location")
class Locations(Resource):
    @ns.marshal_with(location_model)
    def get(self):
        locations = Location.query.all()
        return locations, 200
    
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
        
#DISEASES ROUTES
@ns.route("/diseases")
class Diseases(Resource):
    @ns.marshal_with(disease_model)
    def get(self):
        diseases = Disease.query.all()
        return diseases, 200
    

@ns.route("/diseases/<int:id>")
class DiseasesId(Resource):
    @ns.marshal_with(disease_model)
    def get(self, id):
        diseases = Disease.query.filter_by(id=id).first()
        if diseases:
            return diseases, 200
        else:
            return {"error": "Disease not found"}, 404
        
#DONATIONS ROUTES
@ns.route("/donations")
class Donations(Resource):
    @ns.marshal_with(donation_model)
    def get(self):
        donations = Donation.query.all()
        return donations, 200
    
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
    
@ns.route("/reviews/<int:id>")
class ReviewsId(Resource):
    @ns.marshal_with(review_model)
    def get(self, id):
        reviews = Review.query.filter_by(id=id).first()
        if reviews:
            return reviews, 200
        else:
            return {"error": "Review not found"}, 404
        
