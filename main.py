import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db

# create certificate with credential with the path
cred = credentials.Certificate("./serviceAccountKey.json")

# Initialize the app with service account, granting admin
firebase_admin.initialize_app(cred)

# connect to the database
db=firestore.client()

#Add documents
db.collection('User_Info').document('User_1').set({"Name": "Viv23", "Bio": "Ada Student", "Footprint": "Seattle", "Wishlist": "London"})

# Create a reference for the document before setting
data = {
        "Name": "Tomato25",
        "Bio": "Influencer",
        "Footprint": "Bellevue",
        "Wishlist": ("New York", "Barcelona")
}

# Add a new doc in collection 'User_info' with ID 'User_2'
db.collection('User_Info').document('User_2').set(data)

db.collection('User_Info').add({"Name": "auto", "Bio": "SDE", "Footprint": "Redmond", "Wishlist": ("San Diego", "Paris")})