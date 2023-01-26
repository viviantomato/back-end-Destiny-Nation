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

db.collection('User').add({"Name": "Viv23", "Bio": "Ada Student", "Footprint": "Seattle", "Wishlist": "New York"})



# {
# 	"User1":
# 	{
# 		"Name": "Viv23",
# 		"Bio": "Ada Student",
# 		"Footprint": "Seattle",
#         "Wishlist": "New York"
# 	},
#     "User2":
#     {
#         "Name": "Ann25",
#         "Bio": "Influencer",
#         "Footprint": "Seattl#e",
#         "Wishlist": "San Diego"
#     }
# }