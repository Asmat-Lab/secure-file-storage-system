import os
import base64
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from hash_utils import generate_hash, get_stored_hash

def generate_key_from_password(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def decrypt_file(file_path, password):
    with open(file_path, "rb") as f:
        data = f.read()

    salt = data[:16]
    encrypted = data[16:]

    key = generate_key_from_password(password, salt)
    fernet = Fernet(key)

    try:
        decrypted = fernet.decrypt(encrypted)
    except InvalidToken:
        raise ValueError("Invalid password or corrupted file.")

    filename = os.path.basename(file_path).replace(".enc", "")
    out_dir = "storage/decrypted_files"
    os.makedirs(out_dir, exist_ok=True)
    new_path = os.path.join(out_dir, filename)

    with open(new_path, "wb") as f:
        f.write(decrypted)

    new_hash = generate_hash(new_path)
    stored_hash = get_stored_hash(filename)

    integrity = (stored_hash == new_hash)
    return new_path, integrity