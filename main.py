from encrypt import encrypt_file
from decrypt import decrypt_file

print("1. Encrypt File")
print("2. Decrypt File")

choice = input("Enter choice: ")

if choice == "1":
    file_path = input("Enter file name: ")
    password = input("Enter password: ")
    encrypt_file(file_path, password)

elif choice == "2":
    file_path = input("Enter encrypted file path: ")
    password = input("Enter password: ")
    decrypt_file(file_path, password)

else:
    print("Invalid choice")