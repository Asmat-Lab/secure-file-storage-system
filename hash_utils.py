import hashlib
import os

def generate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

def save_hash(file_name, file_hash):
    os.makedirs("storage", exist_ok=True)
    with open("storage/hashes.txt", "a") as f:
        f.write(f"{file_name}:{file_hash}\n")

def get_stored_hash(file_name):
    hash_file = "storage/hashes.txt"
    if not os.path.exists(hash_file):
        return None
    with open(hash_file, "r") as f:
        for line in f:
            if ":" in line:
                name, hash_val = line.strip().split(":", 1)
                if name == file_name:
                    return hash_val
    return None