from cryptography.fernet import Fernet 

def passwordcryptgraf(password:str):
     key=Fernet.generate_key()
     fernet=Fernet(key=key)
     return fernet.encrypt(password.encode("ASCII"))