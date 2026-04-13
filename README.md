# Secure File Storage System

## Overview
This project is a secure file storage system developed using Python. It ensures confidentiality, integrity, and protection against unauthorized access using encryption and hashing techniques.

## Features
- File Encryption using AES (Fernet)
- Password-Based Key Derivation (PBKDF2)
- File Integrity Verification using SHA-256
- Tamper Detection
- Protection against wrong password access

## Technologies Used
- Python
- Cryptography Library
- Hashlib (SHA-256)

## How It Works
1. User provides a file and password
2. System generates a secure key using PBKDF2
3. File is encrypted and stored securely
4. Hash of the original file is stored
5. During decryption:
   - Password is verified
   - File integrity is checked

## How to Run
1. Install dependencies:
   pip install cryptography

2. Run the program:
   python main.py

## Project Structure
- encrypt.py → handles encryption
- decrypt.py → handles decryption
- hash_utils.py → hashing functions
- storage/ → stores encrypted files and hashes

## Security Concepts Implemented
- Symmetric Encryption (AES)
- Key Derivation (PBKDF2)
- Cryptographic Hashing (SHA-256)
- Integrity Verification

## Author
Asmatullah Baryali