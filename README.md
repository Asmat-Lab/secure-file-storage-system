# Secure File Storage System

## Overview

This project is a secure file storage system built with Python. It keeps your files private and safe from unauthorized access using encryption and hashing.

## Features
* **File Encryption**: Uses AES (Fernet) to lock your files.
* **Secure Keys**: Uses PBKDF2 to turn your password into a strong security key.
* **Integrity Check**: Uses SHA-256 hashing to make sure your files have not been changed.
* **Tamper Detection**: Tells you if someone tried to mess with your data.
* **Wrong Password Protection**: Prevents access if the password is incorrect.

## Technologies Used
* Python
* Cryptography Library
* Hashlib (SHA-256)

## Setup and Installation

### 1. Create a Virtual Environment (.venv)
It is best to run this project in a virtual environment to keep your global Python setup clean.

**Windows (PowerShell or CMD):**
```powershell
python -m venv .venv
```

**Linux / macOS:**
```bash
python3 -m venv .venv
```

### 2. Activate the Environment
You must activate the environment every time you open a new terminal.

**Windows:**
```powershell
.venv\Scripts\activate
```

**Linux / macOS:**
```bash
source .venv/bin/activate
```

### 3. Install Dependencies
Once the environment is active, install the dependencies from the `requirements.txt`:
```bash
pip install -r requirements.txt 
```

### 4. Deactivate
When you are finished working, you can turn off the environment by typing:
```bash
deactivate
```

## Compile The App (Linux)

* **Open the terminal** (usually CTRL+ALT+T) in the project folder
* **Run the following command:**
    ```bash
    pyinstaller --noconfirm --onefile --windowed --name "Secure File Storage System" --add-data "storage:storage" main.py
    ```

***Output:** The executable will be in the dist/ folder.*

## Compile The App (Windows)

* **Open the terminal (Powershell/Command Line)** in the project folder
* **Run the following command:**
    ```bash
    pyinstaller --noconfirm --onefile --windowed --name "Secure File Storage System" --add-data "storage;storage" main.py
    ```
    
***Output:** The executable will be in the dist/ folder.*

## How to Run
1.  Make sure your virtual environment is active.
2.  Run the main program:
    ```bash
    python main.py
    ```

## How It Works
1.  You choose a file and a password.
2.  The system makes a secure key from your password.
3.  The file is encrypted and saved in the `storage/` folder.
4.  The system saves a "fingerprint" (hash) of the original file.
5.  To get your file back, the system checks your password and makes sure the file hasn't been tampered with.

## Project Structure
* `encrypt.py`: Handles locking the files.
* `decrypt.py`: Handles unlocking the files.
* `hash_utils.py`: Checks if files have been changed.
* `storage/`: A folder that holds your encrypted data.

## Author
* Asmatullah Baryali
* Abdulaziz Alhuzami
