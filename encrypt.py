import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from hash_utils import generate_hash, save_hash

def generate_key_from_password(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_file(file_path, password):
    if not os.path.exists(file_path):
        raise FileNotFoundError("Source file not found.")

    salt = os.urandom(16)
    key = generate_key_from_password(password, salt)
    fernet = Fernet(key)

    file_hash = generate_hash(file_path)
    filename = os.path.basename(file_path)
    save_hash(filename, file_hash)

    with open(file_path, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)
    
    out_dir = "storage/encrypted_files"
    os.makedirs(out_dir, exist_ok=True)
    new_path = os.path.join(out_dir, f"{filename}.enc")

    with open(new_path, "wb") as f:
        f.write(salt + encrypted)

    return new_path