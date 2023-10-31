from faker import Faker
import random
from api import app

from api.models import db, Admin, User, Location, Disease, Disease_Location, Review, Donation

with app.app_context():
    fake = Faker()

    Admin.query.delete()
    User.query.delete()
    Location.query.delete()
    Disease.query.delete()
    Disease_Location.query.delete()
    Review.query.delete()
    Donation.query.delete()
    db.session.commit()

    kenyan_counties = [
    "Nairobi",
    "Mombasa",
    "Kwale",
    "Kilifi",
    "Tana River",
    "Lamu",
    "Taita-Taveta",
    "Garissa",
    "Wajir",
    "Mandera",
    "Marsabit",
    "Isiolo",
    "Meru",
    "Tharaka-Nithi",
    "Embu",
    "Kitui",
    "Machakos",
    "Makueni",
    "Nyandarua",
    "Nyeri",
    "Kirinyaga",
    "Murang'a",
    "Kiambu",
    "Turkana",
    "West Pokot",
    "Samburu",
    "Trans-Nzoia",
    "Uasin Gishu",
    "Elgeyo-Marakwet",
    "Nandi",
    "Bungoma",
    "Kakamega",
    "Vihiga",
    "Bomet",
    "Kericho",
    "Kisii",
    "Nyamira",
    "Nairobi City",
    "Diaspora",
    "Kajiado",
    "Kilifi",
    "Nyamira",
    "Nyandarua",
    "Turkana",
    "Wajir",
    "Samburu",
]
    
    common_diseases = [
    "Influenza (Flu)",
    "Common Cold",
    "COVID-19",
    "Hypertension (High Blood Pressure)",
    "Diabetes",
    "Heart Disease",
    "Cancer",
    "Stroke",
    "Asthma",
    "Chronic Obstructive Pulmonary Disease (COPD)",
    "Alzheimer's Disease",
    "Arthritis",
    "Osteoporosis",
    "HIV/AIDS",
    "Malaria",
    "Tuberculosis (TB)",
    "Hepatitis",
    "Epilepsy",
    "Obesity",
    "Anxiety and Depression",
    "Autoimmune Diseases",
    "Gastroesophageal Reflux Disease (GERD)",
    "Chronic Kidney Disease",
    "Allergies",
    "Eczema",
    "Psoriasis",
    "Celiac Disease",
    "Gout",
    "Lupus",
    "Sleep Disorders",
]




    admins = []
    for i in range(10):
        admin = Admin(
            username=fake.user_name(),
            password_hash=fake.password(),
            created_at=fake.date_time(),
            updated_at=fake.date_time(),
        )
        admins.append(admin)
    
    db.session.add_all(admins)
    db.session.commit()

    users = []
    for i in range(20):
        user = User(
            username=fake.name(),
            email=fake.email(),
            password_hash=fake.password(),
            created_at=fake.date_time(),
            updated_at=fake.date_time(),
        )
        users.append(user)

    db.session.add_all(users)
    db.session.commit()

    locations = []
    for i in range(47):
        
        location = Location(
            name = random.choice(kenyan_counties),
            coordinates = random.randint(1, 47),
            population = random.randint(10000, 70000),
            more_details = fake.sentence(),
            created_at=fake.date_time(),
            updated_at=fake.date_time(),
        )
        locations.append(location)

    db.session.add_all(locations)
    db.session.commit()

    diseases = []
    for i in range(20):
        disease = Disease(
            disease_name = random.choice(common_diseases),
            description = fake.paragraph(),
            symptoms = fake.text(),
            treatment = fake.text(),
            prevention = fake.text(),
            num_of_cases=random.randint(20, 50),
        )
        diseases.append(disease)

    db.session.add_all(diseases)
    db.session.commit()

    disease_locations = []
    for i in range(20):
        dl = Disease_Location(
            disease_id = random.randint(1, len(Disease.query.all())),
            location_id = random.randint(1, len(Location.query.all())),
            disease = random.choice(common_diseases),
            location = random.choice(kenyan_counties),
            cases=random.randint(20, 50),
        )
        disease_locations.append(dl)

    db.session.add_all(disease_locations)
    db.session.commit()

    reviews = []
    for i in range(30):
        review = Review(
            user_id = random.randint(1, len(User.query.all())),
            location_id = random.randint(1, len(Location.query.all())),
            review = fake.sentence(),
        )
        reviews.append(review)

    db.session.add_all(reviews)
    db.session.commit()

    donations = []
    for i in range(40):
        donation = Donation(
            amount = random.uniform(10, 500),
            donor_user_id = random.randint(1,len(User.query.all())),
            recipient_location_id = random.randint(1, len(Location.query.all())),
        )
        donations.append(donation)

    db.session.add_all(donations)
    db.session.commit()