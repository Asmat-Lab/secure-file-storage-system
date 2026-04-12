from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
import os
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
    try:
        with open(file_path, "rb") as f:
            data = f.read()

        # Extract salt and encrypted data
        salt = data[:16]
        encrypted = data[16:]

        key = generate_key_from_password(password, salt)
        fernet = Fernet(key)

        decrypted = fernet.decrypt(encrypted)

    except InvalidToken:
        print("❌ ERROR: Wrong password or file tampered!")
        return

    filename = os.path.basename(file_path).replace(".enc", "")
    new_path = f"storage/{filename}"

    with open(new_path, "wb") as f:
        f.write(decrypted)

    # Integrity check
    new_hash = generate_hash(new_path)
    stored_hash = get_stored_hash(filename)

    if stored_hash == new_hash:
        print("✅ File integrity verified")
    else:
        print("❌ File content mismatch")

    print(f"File decrypted and saved as {new_path}")