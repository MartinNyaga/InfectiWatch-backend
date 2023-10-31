from flask_restx import Resource, Namespace
from .models import Admin, User, Location, Disease, Donation, Review, Disease_Location
from .api_models import ( admin_model, user_model, location_model, disease_model, disease_location_model, review_model, donation_model)

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
        
