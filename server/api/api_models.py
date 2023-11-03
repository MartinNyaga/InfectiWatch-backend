from flask_restx import fields
from api import rest_api

# Admin Model
admin_model = rest_api.model("Admin", {
    "id": fields.Integer,
    "username": fields.String,
    "password_hash": fields.String,
    "created_at": fields.DateTime,
    "updated_at": fields.DateTime,
})

# User Model
user_model = rest_api.model("User", {
    "id": fields.Integer,
    "username": fields.String,
    "email": fields.String,
    "password_hash": fields.String,
    "created_at": fields.DateTime,
    "updated_at": fields.DateTime,
    "admin_id": fields.Integer,
})

#Input user model(Create User in sign up)
user_input_model = rest_api.model("User_Input", {
    "username": fields.String,
    "email": fields.String,
    "password_hash": fields.String,
})

#Log in Model
user_login_model = rest_api.model(
    "User_Login",
    {
        "username": fields.String,
        "password_hash": fields.String,
    },
)

# Location Model
location_model = rest_api.model("Location", {
    "id": fields.Integer,
    "name": fields.String,
    "coordinates": fields.String,
    "population": fields.Integer,
    "more_details": fields.String,
    "created_at": fields.DateTime,
    "updated_at": fields.DateTime,
})

#Input Location model
location_input_model = rest_api.model("Location_Input", {
    "name": fields.String,
    "coordinates": fields.String,
    "population": fields.Integer,
    "more_details": fields.String,
})

# Disease Model
disease_model = rest_api.model("Disease", {
    "id": fields.Integer,
    "disease_name": fields.String,
    "description": fields.String,
    "symptoms": fields.String,
    "prevention": fields.String,
    "treatment": fields.String,
    "num_of_cases": fields.Integer,
})

#Input Disease Model
disease_input_model = rest_api.model("Disease_Input", {
    "disease_name": fields.String,
    "description": fields.String,
    "symptoms": fields.String,
    "prevention": fields.String,
    "treatment": fields.String,
    "num_of_cases": fields.Integer,
})

# Disease Location Model
disease_location_model = rest_api.model("DiseaseLocation", {
    "id": fields.Integer,
    "location_id": fields.Integer,
    "disease_id": fields.Integer,
    "disease": fields.String,
    "location": fields.String,
    "cases": fields.Integer,
})

# Review Model
review_model = rest_api.model("Review", {
    "id": fields.Integer,
    "user_id": fields.Integer,
    "location_id": fields.Integer,
    "review": fields.String,
})
#Input Review model
review_input_model = rest_api.model("Review_Input", {
    "user_id": fields.Integer,
    "location_id": fields.Integer,
    "review": fields.String,
})

# Donation Model
donation_model = rest_api.model("Donation", {
    "id": fields.Integer,
    "donor_user_id": fields.Integer,
    "recipient_location_id": fields.Integer,
    "amount": fields.Float,
})

#Input Donation model
donation_input_model = rest_api.model("Donation_Input", {
    "donor_user_id": fields.Integer,
    "recipient_location_id": fields.Integer,
    "amount": fields.Float,
})

#Emergency Model
emergency_model = rest_api.model('Emergency',{
    'id':fields.Integer,
    'condition':fields.String,
    'sender_user_id':fields.Integer,
    'sender_location':fields.Integer,

})

#Input Emergency Model
emergency_input_model=rest_api.model('Emergency_Input',{
    'condition':fields.String,
    'sender_user_id':fields.Integer,
    'sender_location':fields.Integer,
})
