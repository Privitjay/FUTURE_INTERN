import os, io, datetime, logging, base64
from flask import Flask, request, jsonify, send_file, abort
from dotenv import load_dotenv
import jwt, bcrypt
from utils_crypto import encrypt_bytes, decrypt_bytes, b64encode
from models import init_db, add_user, get_user, add_file, list_files, get_file
from werkzeug.utils import secure_filename

# Load environment variables
load_dotenv()
AES_KEY_B64 = os.getenv("AES_SECRET_KEY")
JWT_SECRET = os.getenv("JWT_SECRET")
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
JWT_EXP = int(os.getenv("JWT_EXP_SECONDS", "3600"))

# Ensure upload folder and initialize database
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
init_db()

# Setup logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

app = Flask(__name__)

def create_jwt(username):
    now = datetime.datetime.now(datetime.timezone.utc)
    payload = {
        "sub": username,
        "iat": now,
        "exp": now + datetime.timedelta(seconds=JWT_EXP)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")

def verify_jwt(token):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return payload.get("sub")
    except Exception:
        return None

@app.route('/register', methods=['POST'])
def register():
    data = request.json or {}
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "username and password required"}), 400
    if get_user(username):
        return jsonify({"error": "user exists"}), 400
    ph = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    add_user(username, ph)
    logging.info(f"user registered: {username}")
    return jsonify({"message": "registered"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json or {}
    username = data.get("username")
    password = data.get("password")
    user = get_user(username)
    if not user:
        return jsonify({"error": "invalid credentials"}), 401
    _, uname, pw_hash = user
    if not bcrypt.checkpw(password.encode(), pw_hash.encode()):
        return jsonify({"error": "invalid credentials"}), 401
    token = create_jwt(username)
    logging.info(f"user logged in: {username}")
    return jsonify({"token": token}), 200

@app.route('/upload', methods=['POST'])
def upload():
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return jsonify({"error": "missing token"}), 401
    username = verify_jwt(auth.split(" ",1)[1])
    if not username:
        return jsonify({"error": "invalid token"}), 401
    if 'file' not in request.files:
        return jsonify({"error": "file required"}), 400
    file = request.files['file']
    filename = secure_filename(file.filename)
    if filename == '':
        return jsonify({"error": "invalid filename"}), 400
    data = file.read()
    # encrypt the file bytes
    blob = encrypt_bytes(data, AES_KEY_B64)
    stored_name = f"{datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d%H%M%S')}_{filename}.enc"
    path = os.path.join(UPLOAD_FOLDER, stored_name)
    with open(path, 'wb') as f:
        f.write(blob)
    add_file(filename, stored_name, username, len(data), datetime.datetime.now(datetime.timezone.utc).isoformat())
    logging.info(f"file uploaded by {username}: {filename} -> {stored_name}")
    return jsonify({"message": "uploaded", "stored_name": stored_name}), 201

@app.route('/files', methods=['GET'])
def files():
    # List files (no auth for demo; in production, restrict access)
    items = list_files()
    return jsonify([{"id": r[0], "filename": r[1], "stored_name": r[2], "uploader": r[3], "size": r[4], "created": r[5]} for r in items]), 200

@app.route('/download/<stored_name>', methods=['GET'])
def download(stored_name):
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return jsonify({"error": "missing token"}), 401
    username = verify_jwt(auth.split(" ",1)[1])
    if not username:
        return jsonify({"error": "invalid token"}), 401

    record = get_file(stored_name)
    if not record:
        return jsonify({"error": "file not found"}), 404
    # In a real app, enforce uploader==username or admin rights
    path = os.path.join(UPLOAD_FOLDER, stored_name)
    if not os.path.exists(path):
        return jsonify({"error": "file not found"}), 404
    with open(path, 'rb') as f:
        blob = f.read()
    plaintext = decrypt_bytes(blob, AES_KEY_B64)
    logging.info(f"file downloaded by {username}: {stored_name}")
    return send_file(io.BytesIO(plaintext), as_attachment=True, download_name=record[1])

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "AES File Portal running"}), 200

if __name__ == "__main__":
    # Run with adhoc TLS for local HTTPS
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), ssl_context='adhoc', debug=True)
