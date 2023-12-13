from faker import Faker
import random
from api import app

from api.models import db, User, Location, Disease, Disease_Location, Review, Donation, Emergency

with app.app_context():
    fake = Faker()

    
    User.query.delete()
    Location.query.delete()
    Disease.query.delete()
    Disease_Location.query.delete()
    Review.query.delete()
    Donation.query.delete()
    db.session.commit()

    kenyan_counties_data = [
    {
        "name": "Nairobi",
        "coordinates": "1",
        "population": 4397073,
        "more_details": "Capital city of Kenya",
    },
    {
        "name": "Mombasa",
        "coordinates": "2",
        "population": 1208333,
        "more_details": "Coastal city and major port",
    },
    {
        "name": "Kwale",
        "coordinates": "3",
        "population": 866820,
        "more_details": "Coastal county with diverse ecosystems",
    },
    {
        "name": "Kilifi",
        "coordinates": "4",
        "population": 1453787,
        "more_details": "Known for its beautiful beaches",
    },
    {
        "name": "Tana River",
        "coordinates": "5",
        "population": 315943,
        "more_details": "Located along the Tana River",
    },
    {
        "name": "Lamu",
        "coordinates": "6",
        "population": 143920,
        "more_details": "Historic town with Swahili architecture",
    },
    {
        "name": "Taita-Taveta",
        "coordinates": "7",
        "population": 340671,
        "more_details": "Rich in biodiversity and wildlife",
    },
    {
        "name": "Garissa",
        "coordinates": "8",
        "population": 841353,
        "more_details": "Major commercial and cultural center",
    },
    {
        "name": "Wajir",
        "coordinates": "9",
        "population": 781263,
        "more_details": "Known for its arid landscape",
    },
    {
        "name": "Mandera",
        "coordinates": "10",
        "population": 867457,
        "more_details": "Located in the northeastern part of Kenya",
    },
    {
        "name": "Marsabit",
        "coordinates": "11",
        "population": 459785,
        "more_details": "Home to Marsabit National Park",
    },
    {
        "name": "Isiolo",
        "coordinates": "12",
        "population": 268002,
        "more_details": "Gateway to the northern Kenya safari circuit",
    },
    {
        "name": "Meru",
        "coordinates": "13",
        "population": 1545714,
        "more_details": "Agricultural and tourism hub",
    },
    {
        "name": "Tharaka-Nithi",
        "coordinates": "14",
        "population": 393177,
        "more_details": "Known for Tharaka cultural heritage",
    },
    {
        "name": "Embu",
        "coordinates": "15",
        "population": 608599,
        "more_details": "Agricultural and business center",
    },
    {
        "name": "Kitui",
        "coordinates": "16",
        "population": 1139916,
        "more_details": "Rich in minerals and coal deposits",
    },
    {
        "name": "Machakos",
        "coordinates": "17",
        "population": 1421932,
        "more_details": "Part of the Nairobi Metropolitan region",
    },
    {
        "name": "Makueni",
        "coordinates": "18",
        "population": 987653,
        "more_details": "Known for the Tsavo East National Park",
    },
    {
        "name": "Nyandarua",
        "coordinates": "19",
        "population": 638289,
        "more_details": "Agricultural county in the central region",
    },
    {
        "name": "Nyeri",
        "coordinates": "20",
        "population": 759164,
        "more_details": "Rich in agriculture and tourism",
    },
    {
        "name": "Kirinyaga",
        "coordinates": "21",
        "population": 610411,
        "more_details": "Agricultural and horticultural activities",
    },
    {
        "name": "Murang'a",
        "coordinates": "22",
        "population": 1056640,
        "more_details": "Known for coffee and tea farming",
    },
    {
        "name": "Kiambu",
        "coordinates": "23",
        "population": 2417735,
        "more_details": "Part of the Nairobi Metropolitan region",
    },
    {
        "name": "Turkana",
        "coordinates": "24",
        "population": 926976,
        "more_details": "Largest county in Kenya with diverse landscapes",
    },
    {
        "name": "West Pokot",
        "coordinates": "25",
        "population": 621241,
        "more_details": "Rich in minerals and wildlife",
    },
    {
        "name": "Samburu",
        "coordinates": "26",
        "population": 310327,
        "more_details": "Known for Samburu National Reserve",
    },
    {
        "name": "Trans-Nzoia",
        "coordinates": "27",
        "population": 818757,
        "more_details": "Agricultural county in the Rift Valley",
    },
    {
        "name": "Uasin Gishu",
        "coordinates": "28",
        "population": 1163186,
        "more_details": "Agricultural and industrial hub",
    },
    {
        "name": "Elgeyo-Marakwet",
        "coordinates": "29",
        "population": 454480,
        "more_details": "Known for the Kerio Valley",
    },
    {
        "name": "Nandi",
        "coordinates": "30",
        "population": 885711,
        "more_details": "Agricultural county in the Rift Valley",
    },
    {
        "name": "Bungoma",
        "coordinates": "31",
        "population": 1699581,
        "more_details": "Agricultural county with diverse cultures",
    },
    {
        "name": "Kakamega",
        "coordinates": "32",
        "population": 1867570,
        "more_details": "Known for Kakamega Forest",
    },
    {
        "name": "Vihiga",
        "coordinates": "33",
        "population": 590013,
        "more_details": "Known for its hills and agricultural activities",
    },
    {
        "name": "Bomet",
        "coordinates": "34",
        "population": 875689,
        "more_details": "Agricultural and tea farming county",
    },
    {
        "name": "Kericho",
        "coordinates": "35",
        "population": 901777,
        "more_details": "Known for tea and tourism",
    },
    {
        "name": "Kisii",
        "coordinates": "36",
        "population": 1233823,
        "more_details": "Known for soapstone mining",
    },
    {
        "name": "Nyamira",
        "coordinates": "37",
        "population": 605576,
        "more_details": "Known for banana and tea farming",
    },
    {
        "name": "Nairobi City",
        "coordinates": "38",
        "population": 4397073,
        "more_details": "Capital city of Kenya",
    },
    {
        "name": "Diaspora",
        "coordinates": "39",
        "population": 0,  # Placeholder for Diaspora
        "more_details": "Kenyan diaspora communities around the world",
    },
    {
        "name": "Kajiado",
        "coordinates": "40",
        "population": 1077730,
        "more_details": "Known for Amboseli National Park",
    },
    {
        "name": "Kilifi",
        "coordinates": "41",
        "population": 1453787,
        "more_details": "Known for its beautiful beaches",
    },
    {
        "name": "Nyamira",
        "coordinates": "42",
        "population": 605576,
        "more_details": "Known for banana and tea farming",
    },
    {
        "name": "Nyandarua",
        "coordinates": "43",
        "population": 638289,
        "more_details": "Agricultural county in the central region",
    },
    {
        "name": "Turkana",
        "coordinates": "44",
        "population": 926976,
        "more_details": "Largest county in Kenya with diverse landscapes",
    },
    {
        "name": "Wajir",
        "coordinates": "45",
        "population": 781263,
        "more_details": "Known for its arid landscape",
    },
    {
        "name": "Samburu",
        "coordinates": "46",
        "population": 310327,
        "more_details": "Known for Samburu National Reserve",
    },
]



    
    disease_data = [
    {
        "disease_name": "Influenza (Flu)",
        "description": "Influenza, commonly known as the flu, is a viral infection that attacks the respiratory system.",
        "symptoms": "Symptoms include fever, cough, sore throat, body aches, fatigue, and more.",
        "prevention": "Preventive measures include annual vaccination, practicing good hygiene, and avoiding close contact with infected individuals.",
        "treatment": "Treatment may involve antiviral medications, rest, and symptom management."
    },
    {
        "disease_name": "Common Cold",
        "description": "The common cold is a viral infection affecting the upper respiratory tract.",
        "symptoms": "Symptoms include a runny or stuffy nose, sneezing, coughing, and mild body aches.",
        "prevention": "Preventive measures include frequent handwashing, avoiding close contact with sick individuals, and maintaining a healthy lifestyle.",
        "treatment": "Treatment involves rest, staying hydrated, and over-the-counter medications for symptom relief."
    },
    {
        "disease_name": "COVID-19",
        "description": "COVID-19 is a respiratory illness caused by the SARS-CoV-2 virus.",
        "symptoms": "Symptoms range from mild to severe and may include fever, cough, shortness of breath, loss of taste or smell, and fatigue.",
        "prevention": "Preventive measures include vaccination, wearing masks, practicing social distancing, and frequent handwashing.",
        "treatment": "Treatment varies and may include supportive care, antiviral medications, and hospitalization in severe cases."
    },
    {
        "disease_name": "Hypertension (High Blood Pressure)",
        "description": "Hypertension is a condition in which the force of blood against the artery walls is consistently too high.",
        "symptoms": "Hypertension is often asymptomatic, but severe cases may lead to headaches, shortness of breath, or nosebleeds.",
        "prevention": "Preventive measures include maintaining a healthy diet, regular exercise, limiting alcohol intake, and managing stress.",
        "treatment": "Treatment may involve lifestyle changes, medication, and regular monitoring of blood pressure."
    },
    {
        "disease_name": "Diabetes",
        "description": "Diabetes is a chronic condition that affects how your body turns food into energy.",
        "symptoms": "Symptoms include increased thirst, frequent urination, unexplained weight loss, and fatigue.",
        "prevention": "Preventive measures include a healthy diet, regular exercise, maintaining a healthy weight, and monitoring blood sugar levels.",
        "treatment": "Treatment involves medication, insulin therapy, and lifestyle changes to manage blood sugar levels."
    },
    {
        "disease_name": "Heart Disease",
        "description": "Heart disease refers to a range of conditions that affect your heart.",
        "symptoms": "Symptoms vary but may include chest pain, shortness of breath, fatigue, and irregular heartbeat.",
        "prevention": "Preventive measures include a healthy diet, regular exercise, not smoking, and managing stress.",
        "treatment": "Treatment may involve medication, lifestyle changes, or surgical procedures depending on the specific heart condition."
    },
    {
        "disease_name": "Cancer",
        "description": "Cancer is a group of diseases characterized by the uncontrolled growth and spread of abnormal cells.",
        "symptoms": "Symptoms depend on the type of cancer but may include lumps, changes in bowel or bladder habits, persistent cough, and unexplained weight loss.",
        "prevention": "Preventive measures include avoiding tobacco, maintaining a healthy diet, regular exercise, and early detection through screenings.",
        "treatment": "Treatment varies and may include surgery, chemotherapy, radiation, immunotherapy, or a combination of these."
    },
    {
        "disease_name": "Stroke",
        "description": "A stroke occurs when there is a disruption of blood flow to the brain, leading to brain cell damage.",
        "symptoms": "Symptoms include sudden numbness or weakness, confusion, trouble speaking or understanding speech, and severe headache.",
        "prevention": "Preventive measures include maintaining a healthy diet, regular exercise, managing high blood pressure, and not smoking.",
        "treatment": "Treatment depends on the type of stroke and may involve medication, surgery, or rehabilitation."
    },
    {
        "disease_name": "Asthma",
        "description": "Asthma is a chronic respiratory condition characterized by inflammation of the airways.",
        "symptoms": "Symptoms include wheezing, shortness of breath, chest tightness, and coughing, especially at night or early morning.",
        "prevention": "Preventive measures include avoiding triggers, using prescribed medications, and having an asthma action plan.",
        "treatment": "Treatment involves long-term control medications and quick-relief (rescue) medications to manage symptoms."
    },
    {
        "disease_name": "Chronic Obstructive Pulmonary Disease (COPD)",
        "description": "COPD is a group of progressive lung diseases, including chronic bronchitis and emphysema, that make it hard to breathe.",
        "symptoms": "Symptoms include shortness of breath, chronic cough, wheezing, and chest tightness.",
        "prevention": "Preventive measures include smoking cessation, avoiding environmental pollutants, and managing symptoms with medication.",
        "treatment": "Treatment involves medication, pulmonary rehabilitation, oxygen therapy, and, in severe cases, surgery."
    },
    {
        "disease_name": "Alzheimer's Disease",
        "description": "Alzheimer's disease is a progressive brain disorder that affects memory, thinking, and behavior.",
        "symptoms": "Symptoms include memory loss, confusion, difficulty communicating, and changes in behavior.",
        "prevention": "While there is no known prevention, staying mentally and physically active, managing cardiovascular risk factors, and maintaining a healthy lifestyle may help.",
        "treatment": "Treatment aims to manage symptoms and may involve medications and support services."
    },
    {
        "disease_name": "Arthritis",
        "description": "Arthritis is inflammation of one or more joints, leading to pain and stiffness.",
        "symptoms": "Symptoms include joint pain, swelling, and stiffness, which can worsen with age.",
        "prevention": "Preventive measures include maintaining a healthy weight, staying active, and protecting joints from injury.",
        "treatment": "Treatment involves medication, physical therapy, and lifestyle changes to manage symptoms and improve joint function."
    },
    {
        "disease_name": "Osteoporosis",
        "description": "Osteoporosis is a condition characterized by weak, brittle bones that are more prone to fractures.",
        "symptoms": "Osteoporosis is often asymptomatic until a fracture occurs. Fractures, especially in the spine or hip, are common.",
        "prevention": "Preventive measures include a diet rich in calcium and vitamin D, regular weight-bearing exercise, and lifestyle changes to reduce the"}]






    users = []
    for i in range(20):
        user = User(
            username=fake.name(),
            email=fake.email(),
            password_hash=fake.password(),
            # role_id = random.randint(1, len(Role.query.all())),
            created_at=fake.date_time(),
            updated_at=fake.date_time(),
        )
        users.append(user)

    db.session.add_all(users)
    db.session.commit()

    locations = []
    for county_data in kenyan_counties_data:
        location = Location(
            name=county_data["name"],
            coordinates=county_data["coordinates"],
            population=county_data["population"],
            more_details=county_data["more_details"],
            created_at=fake.date_time(),
            updated_at=fake.date_time(),
        )
        locations.append(location)

    db.session.add_all(locations)
    db.session.commit()

    diseases = []
    for disease_data in disease_data:
        disease = Disease(
            disease_name=disease_data.get("disease_name", ""),
            description=disease_data.get("description", ""),
            symptoms=disease_data.get("symptoms", ""),
            prevention=disease_data.get("prevention", ""),
            treatment=disease_data.get("treatment", ""),
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
            disease = fake.name(),
            location = fake.name(),
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

    emergencies = []
    for i in range(10):
        emergency = Emergency(
            condition = fake.name(),
            sender_user_id = random.randint(1, len(User.query.all())),
            sender_location = random.randint(1, len(Location.query.all())),
        )
        emergencies.append(emergency)

    db.session.add_all(emergencies)
    db.session.commit()