import hashlib

# Generate hash of file
def generate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


# Save hash
def save_hash(file_name, file_hash):
    with open("storage/hashes.txt", "a") as f:
        f.write(f"{file_name}:{file_hash}\n")


# Get stored hash
def get_stored_hash(file_name):
    try:
        with open("storage/hashes.txt", "r") as f:
            for line in f:
                name, hash_val = line.strip().split(":")
                if name == file_name:
                    return hash_val
    except FileNotFoundError:
        return None

    return None