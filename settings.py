from flask_cors import CORS
from database.db import initialize_db
from app.api import app

CORS(app)
app.config["MONGODB_SETTINGS"] = {
    "host": "mongodb+srv://inca-bat:XiawjppUTwLSZ2vN@inca-bat.1uc54.mongodb.net/inca-bat"
}

app.config["MONGO_CONNECT"] = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

initialize_db(app)
