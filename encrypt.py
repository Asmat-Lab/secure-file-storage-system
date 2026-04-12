from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
import os
from hash_utils import generate_hash, save_hash

# Generate key from password
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
    # Generate random salt
    salt = os.urandom(16)

    key = generate_key_from_password(password, salt)
    fernet = Fernet(key)

    # Hash before encryption
    file_hash = generate_hash(file_path)
    filename = os.path.basename(file_path)
    save_hash(filename, file_hash)

    with open(file_path, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    new_path = f"storage/encrypted_files/{filename}.enc"

    # Save salt + encrypted data together
    with open(new_path, "wb") as f:
        f.write(salt + encrypted)

    print(f"File encrypted and saved as {new_path}")