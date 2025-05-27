import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get MongoDB URI from environment
mongo_uri = os.getenv("MONGO_URI")

# Create MongoDB client
client = MongoClient(mongo_uri)

# Choose your database and collection
db = client["face_recognition_db"]
faces_collection = db["faces"]

# Example: Save face data
def save_face(name, embedding):
    face_data = {
        "name": name,
        "embedding": embedding
    }
    result = faces_collection.insert_one(face_data)
    return str(result.inserted_id)

# Example: Get all faces
def get_all_faces():
    return list(faces_collection.find({}, {"_id": 0}))
