import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def derive_key(password: str, salt: bytes) -> bytes:
    """Derive a Fernet key from the master password and salt."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

# 🔐 Ask for master password
master_pwd = input("What is the master password? ")

# 🔐 Load or create salt
if not os.path.exists("salt.salt"):
    with open("salt.salt", "wb") as f:
        f.write(os.random(16))

with open("salt.salt", "rb") as f:
    salt = f.read()

# ✅ Derive encryption key from password
key = derive_key(master_pwd, salt)
fer = Fernet(key)

def view():
    try:
        with open('password.txt', 'r') as f:
            for line in f.readlines():
                data = line.strip()
                if not data:
                    continue
                user, encrypted = data.split("|")
                decrypted = fer.decrypt(encrypted.encode()).decode()
                print(f"🔐 Account: {user} | Password: {decrypted}")
    except Exception as e:
        print(f"❌ Error while reading passwords: {e}")

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()

    with open('password.txt', 'a') as f:
        f.write(f"{name}|{encrypted_pwd}\n")
    print("✅ Password saved successfully.")

# 🧠 Main loop
while True:
    mode = input("\nWould you like to add a new password or view existing ones (view, add), press q to quit? ").lower()

    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "q":
        break
    else:
        print("❌ Invalid mode. Try again.")
